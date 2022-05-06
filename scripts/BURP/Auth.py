#coding: utf-8
#
### CREATED BY KARMAZ
#
#
### TO DO:
#   1. More policies (checks).
#   2. IDOR module.
#   3. Additionall headers (not auth).
#   4. Rebuild on GOlang and go async.
### FUNCTIONS:
#
# 1. Load URLs from the wordlist to memory. 
# 2. Load SIDs (cookies|headers):
# 3. Test broken access control on each URL with different methods
#       - GET
#       - POST
#       - HEAD
#       - DELETE
#       - PATCH
# - - - - - - -
#       - PUT
#       - TRACE
#       - CONNECT
#       - XD
#       - xd
#
#### WORKFLOW
# 1. Copy URLs from Burp target scope.
# 2. Start the python3 crimson_authorize.py -w "urls.txt" -c "a=1,b=2;" | -H "user_2: API_KEY1" -H "user_2: API_KEY2"
# 3. Check the output.
#
###

from dataclasses import asdict
import optparse,requests,json
from difflib import SequenceMatcher

def similar(a, b):
    '''Check similarity between two strings.'''
    return SequenceMatcher(None, a, b).ratio()


def parse_cookie(c):
    '''Parse single cookie header for REQUESTS module: "a=1,b=2;" => {'a': '1', 'b': '2'}'''
    cookies = c.replace(";","").replace(",","=").split("=")
    i = 0
    k,v = [],[]
    for cookie in cookies:
        if i%2==0:
            k.append(cookie)
            i+=1
        else:
            v.append(cookie)
            i+=1
    cookies = dict(zip(k,v))
    return cookies


def parse_header(h):
    '''Parse single header for REQUESTS module: "H1:a" => {'H1': 'a'} - NO SPACES! H1:_<-here '''
    k,v= [],[]
    headers = h.split(":")
    k.append(headers[0])
    v.append(headers[1])
    headers = dict(zip(k,v))
    return headers


def parse_auths(c,h):
    '''Works only for single auth method headers | cookies.'''
    auths_c,auths_h = [], []
    if c != None:
        for cookie in c:
            cookies = parse_cookie(cookie)
            auths_c.append(cookies)
    if h != None:
        for header in h:
            headers = parse_header(header)
            auths_h.append(headers)
    return auths_c,auths_h


def ba_requests(c,h,methods):
    '''Make all requests auth & unauth => return responses in dict.'''
    r = {}
    auths = []
    if c != []:
        auths = c
    elif h != []:
        auths = h
    auths.append("UNAUTH")
    for auth in auths:
        k = str(auth)
        a = []
        for method in methods:
            if (auth != "UNAUTH" and c != []): # Check cookies auth.
                m = getattr(requests,method)
                try:
                    a.append(m(url.rstrip(),cookies=auth,verify=False))
                except:
                    print("Connection error to " + url.rstrip())
            elif (auth != "UNAUTH" and h != []): # Check header auth.
                m = getattr(requests,method)
                try:
                    a.append(m(url.rstrip(),headers=auth,verify=False))
                except:
                    print("Connection error to " + url.rstrip())
            else: # Check UNAUTH in the last iteration.
                m = getattr(requests,method)
                try:
                    a.append(m(url.rstrip(),verify=False))
                except:
                    print("Connection error to " + url.rstrip())
        r[k]=a
    return r


def ba_analyzer(requests_objects):
    '''Read all requests and find potentiall misconfigurations.'''
    prev_auth = []
    out_status = []
    out_body = []
    for auth in requests_objects:
        if auth != "UNAUTH":
            i = 0
            for r in requests_objects[auth]: # CHECKS HERE
                unauth = (requests_objects["UNAUTH"][i])
                # If there is more than one auth cookie | auth header check mutations auth1&auth2, auth1&auth3, auth2&auth3...:
                if prev_auth != []:
                    for prev in prev_auth:
                        # STATUS CODE
                        if r.status_code == requests_objects[prev][i].status_code:
                            print("STATUS | " + prev +"&"+ auth + " | " + str(r.status_code) + " | " + r.url)
                            out_status.append("STATUS | " + prev +"&"+ auth + " | " + str(r.status_code) + " | " + r.url)
                        # BODY 95 %
                        if similar(r.text,requests_objects[prev][i].text) > 0.95:
                            print("BODY   | " + prev +"&"+ auth + " | " + r.url)
                            out_body.append("BODY   | " + prev +"&"+ auth + " | " + r.url)
                # CHECK UNAUTH
                if r.status_code == unauth.status_code:
                    print("STATUS | UNAUTH&"+ auth + " | " + str(r.status_code) + " | " + r.url)
                    out_status.append("STATUS | UNAUTH&"+ auth + " | " + str(r.status_code) + " | " + r.url)
                # BODY 95% 
                if similar(r.text,unauth.text) > 0.95:
                    print("BODY   | UNAUTH&"+ auth + " | " + r.url)
                    out_body.append("BODY   | UNAUTH&"+ auth + " | " + r.url)
                i+=1
        prev_auth.append(auth)
    return out_status, out_body


def save_log(filename,log):
    with open(filename,"a") as f:
        for l in log:
            f.write(l + "\n")

# OPTIONS
parser = optparse.OptionParser()
parser.add_option('-c', '--cookie', action="append")
parser.add_option('-H', '--header', action="append")
parser.add_option('-w', '--wordlist', action="store")
parser.add_option('-o', '--out', action="store")
options, args = parser.parse_args()

# MAIN
c = options.cookie
h = options.header
c,h = parse_auths(c,h)
m = ["get","post","head","delete","patch"]

with open(options.wordlist,"r") as urls:
    for url in urls:
        r = ba_requests(c,h,m)

s,b = ba_analyzer(r)

if options.out != None:
    save_log(options.out,s)
    save_log(options.out,b)