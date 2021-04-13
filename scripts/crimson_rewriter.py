# coding: utf-8
#
#
### CREATED BY KARMAZ
#
### FUNCTIONS
#
# 1. CHECK IF X-Original-Url AND X-Rewrite-Url IS HANDLED BY THE SERVER
#
###

import sys, getopt, requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from tqdm import tqdm

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
██████╗ ███████╗██╗    ██╗██████╗ ██╗████████╗███████╗██████╗ 
██╔══██╗██╔════╝██║    ██║██╔══██╗██║╚══██╔══╝██╔════╝██╔══██╗
██████╔╝█████╗  ██║ █╗ ██║██████╔╝██║   ██║   █████╗  ██████╔╝
██╔══██╗██╔══╝  ██║███╗██║██╔══██╗██║   ██║   ██╔══╝  ██╔══██╗
██║  ██║███████╗╚███╔███╔╝██║  ██║██║   ██║   ███████╗██║  ██║
╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝\033[0m""")
    print("\nUSAGE: python crimson_rewriter.py -w [wordlist_with_urls] -H [headers] -c [Cookie: a=1;] -h [show_help]")

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

def rewriter_check(urls,headers,cookies):
    output_list = []
    print("\033[0;31m [+]\033[0m REWRITER PROGRESS")
    for url in tqdm(urls):
        try:
            r1 = requests.get(url.rstrip(), verify=False)
            r2 = requests.get(url.rstrip(), verify=False, headers={'X-Original-Url':'/doesnotextist123'})
            r3 = requests.get(url.rstrip(), verify=False, headers={'X-Rewrite-Url':'/doesnotexist321'})
            if r1.status_code != r2.status_code:
                output_list.append("[+] ORIGINAL HEADER FOUND: " + r2.url)
            elif r1.status_code != r3.status_code:
                output_list.append("[+] REWRITE HEADER FOUND: " + r1.url)
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            pass
    return output_list


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
    if current_argument in ("-w", "--wordlist"):
        list_of_urls = current_value
    elif current_argument in ("-c", "--cookies"):
        cookies = current_value
    elif current_argument in ("-H", "--header"):
        headers.update([current_value.split("=")])
    elif current_argument in ("-o", "--output"):
        output = current_value
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
        output_list = rewriter_check(urls, headers, cookies)
        if logs_name is not None:
            logs_saver(output_list, logs_name)
        else:
            for element in output_list:
                print(element.rstrip())
