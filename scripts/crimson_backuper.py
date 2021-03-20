# coding: utf-8
#
### CREATED BY KARMAZ
#
#
### FUNCTIONS:
#
# 1. CHECK BACKUPS OF KNOWN FILES
#
###
# USAGE EXAMPLE:
#
###

import sys, getopt, requests, re, urllib3
from collections import Counter
from http.cookies import SimpleCookie
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

### OPTIONS ---
argument_list = sys.argv[1:]
short_options = "w:c:h:e:"
long_options = ["wordlist", "cookies", "header", "extensions"]
try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    sys.exit(2)
### --- (They will be iterated at the bottom of the screen ---

def helper():
    '''Print usage in case of wrong options or arguments being used'''
    print("""\033[0;31m
██████╗  █████╗  ██████╗██╗  ██╗██╗   ██╗██████╗ ███████╗██████╗
██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║   ██║██╔══██╗██╔════╝██╔══██╗
██████╔╝███████║██║     █████╔╝ ██║   ██║██████╔╝█████╗  ██████╔╝
██╔══██╗██╔══██║██║     ██╔═██╗ ██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗
██████╔╝██║  ██║╚██████╗██║  ██╗╚██████╔╝██║     ███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝\033[0m""")
    print("\nUSAGE: python crimson_backuper.py -w [wordlist_with_urls] -h [optional_headers]")

def import_wordlist(wordlist_filepath):
    '''Importing wordlist line by line into an array'''
    with open(wordlist_filepath) as f:
        new_wordlist = [",".join(line.split(",")).strip() for line in f.readlines()]
    return new_wordlist

def import_cookies(cookie_data):
    '''Importing cookies from header f.e. "Cookie: auth1=qwe; auth2=asd;" '''
    cookie = SimpleCookie()
    cookie.load(cookie)
    cookies = dict((key, morsel.value) for key, morsel in cookie.items())
    return cookies

def combine_wordlists(wordlist1, wordlist2):
    '''Join strings one by one from array1 with array2'''
    return [w1 + w2 for w1 in wordlist1 for w2 in wordlist2]

def check_backup_file(wordlist1, wordlist2, cookies, headers):
    '''Combine urls with extension wordlist and check for backup files'''
    s = requests.Session()
    s.cookies.update(cookies)
    s.headers.update(headers)
    r1 = s.get(wordlist1[0], allow_redirects=True, verify=False)
    print r1.status_code
    print r1.headers
    #print r1.text
    print r1.ok
    #print r1.content
    print r1.is_permanent_redirect
    print r1.is_redirect
    print r1.reason
    print ("======================")
    r2 = s.get(wordlist2[0], allow_redirects=True, verify=False)
    print r2.status_code
    print r2.headers
    #print r2.text
    print r2.ok
    #print r2.content
    print r2.is_redirect
    print r2.reason
    print r2.url
    
    r2 = s.get(wordlist2[0], allow_redirects=True, verify=False)
    # If backup file is permanently redirected step into next check.
   
    if not r2.is_permanent_redirect:
        # If 
        r1 = s.get(wordlist1[0], allow_redirects=True, verify=False)
        # If status code of r2 is the same as r1, or status code of r2 is equal 200 step into next check.
        if r2.status_code == r1.status_code or r2.stauts_code == 200:
            # If Content-Length or the r2 is not the same, step into next check.
            if r2.headers['Content-Length'] != r1.headers['Content-Length']:
                pass

### OPTIONS ---
headers = {}
for current_argument, current_value in arguments:
    if current_argument in ("-w", "--wordlist"):
        list_of_urls = current_value
    elif current_argument in ("-c", "--cookies"):
        cookies = current_value
    elif current_argument in ("-h", "--header"):
        headers.update([current_value.split("=")])
    elif current_argument in ("-e", "--extensions"):
        list_of_extensions = current_value

### MAIN
if __name__ == '__main__':
    try:
        urls = import_wordlist(list_of_urls)
        extensions = import_wordlist(list_of_extensions)
        cookies = import_cookies(cookies)
        backups = combine_wordlists(urls, extensions)
        check_backup_file(urls, backups, cookies, headers)
    except:
        helper()
