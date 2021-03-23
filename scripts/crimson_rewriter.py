# coding: utf-8
#
### CREATED BY KARMAZ
#
#
### TO DO
# 1. Add authorization bearer / cookie header
### FUNCTIONS
#
# 1. CHECK IF X-Original-Url AND X-Rewrite-Url IS HANDLED BY THE SERVER
#
### WORKFLOW
# 0. Create wordlist with URLS - "all.txt"
# 1. Start the script: python3 crimson_rewriter.py
###

import sys, getopt, requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


### OPTIONS ---
argument_list = sys.argv[1:]
short_options = "w:c:H:e:h"
long_options = ["wordlist", "cookies", "header", "extensions", "help"]
try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    print(err)
    sys.exit(2)
### --- (They will be iterated at the bottom of the screen ---

def helper():
    '''Print usage in case of wrong options or arguments being used'''
    print("""\033[0;31m

 ██████╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗ 
██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██╔══██╗
██║   ██║██████╔╝█████╗  ██╔██╗ ██║█████╗  ██████╔╝
██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╔╝██║     ███████╗██║ ╚████║███████╗██║  ██║
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝\033[0m""")
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
    original = []
    rewrite = []
    print("[*] CURENTLY TESTING")
    for url in urls:
        try:
            print(url.rstrip())
            r1 = requests.get(url.rstrip(), verify=False)
            r2 = requests.get(url.rstrip(), verify=False, headers={'X-Original-Url':'/doesnotextist123'})
            r3 = requests.get(url.rstrip(), verify=False, headers={'X-Rewrite-Url':'/doesnotexist321'})
            if r1.status_code != r2.status_code:
                original.append(url)
            elif r1.status_code != r3.status_code:
                rewrite.append(url)
        except:
            pass

    print("[*] VULNERABLE\n")
    print("[*] X-Rewrite-Url:\n")
    print(*rewrite, sep='\n')
    print("\n[*] X-Original-Url:\n")
    print(*original, sep='\n')


### OPTIONS ---
headers = {}
cookies ={}
show_help = False
for current_argument, current_value in arguments:
    if current_argument in ("-w", "--wordlist"):
        list_of_urls = current_value
    elif current_argument in ("-c", "--cookies"):
        cookies = current_value
    elif current_argument in ("-H", "--header"):
        headers.update([current_value.split("=")])
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
        rewriter_check(urls,headers,cookies)
