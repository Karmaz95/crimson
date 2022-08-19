# coding: utf-8
#
### CREATED BY KARMAZ
#
#
### TO DO:
#
### FUNCTIONS:
# 
# 1. This tools takes the URL and swap the argument for the given payload.
# 2. It is practial for testing manually XSS and other vulns evaluated during page load.
#
# F.e.          http://url?a1=x&a2=y
#       1)      http://url?a1=[payload]&a2=y
#       2)      http://url?a1=x&a2=[payload]
###
# USAGE EXAMPLE:
#   python crimson_paramjuggler.py -u [url] -l [wordlist] -p [payload]
#
###

import webbrowser
import sys
import time
import getopt
#import urlparse
from urllib.parse import urlparse
from urllib.parse import urlunparse

### OPTIONS ---
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
short_options = "hu:l:p:"
long_options = ["help", "url", "list", "payload"]
try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
        sys.exit(2)
### --- (They will be iterated at the bottom of the screen ---


### REPLACE PARAMS WITH PAYLOAD => print value to stdout
def paramjuggler(url,payload):
    #parsed=urlparse.urlparse(url)
    parsed=urlparse(url)
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
        #result.append(urlparse.urlunparse(new_parsed))
        result.append(urlunparse(new_parsed))
        print("".join(result).rstrip())


### READ URLS
def read_urls(list_of_urls):
    with open(list_of_urls) as urls:
        for url in urls:
            paramjuggler(url,payload)

def print_help():
    print("""
██████╗  █████╗ ██████╗  █████╗ ███╗   ███╗     ██╗██╗   ██╗ ██████╗  ██████╗ ██╗     ███████╗██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗ ████║     ██║██║   ██║██╔════╝ ██╔════╝ ██║     ██╔════╝██╔══██╗
██████╔╝███████║██████╔╝███████║██╔████╔██║     ██║██║   ██║██║  ███╗██║  ███╗██║     █████╗  ██████╔╝
██╔═══╝ ██╔══██║██╔══██╗██╔══██║██║╚██╔╝██║██   ██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝  ██╔══██╗
██║     ██║  ██║██║  ██║██║  ██║██║ ╚═╝ ██║╚█████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚════╝  ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝""")
    print("\tUSAGE: \tcrimson_paramjuggler.py\n\n \t\t-h --help => Show this help \n\t\t-u --url=\"http://example.com?x1=lol1&x2=lol2\" \n\t\t-l --list=[list of urls]\n\t\t-p --[payload to use]")



### OPTIONS ---
for current_argument, current_value in arguments:
    if current_argument in ("-h", "--help"):
        print_help()
    elif current_argument in ("-u", "--url"):
        url=current_value
    elif current_argument in ("-l", "--list"):
        list_of_urls=current_value
    elif current_argument in ("-p", "--payload"):
        payload=current_value
### ---

try: list_of_urls
except NameError: list_of_urls = None

if list_of_urls is None:
    try:
        paramjuggler(url,payload)
    except:
        pass
else:
    read_urls(list_of_urls)
