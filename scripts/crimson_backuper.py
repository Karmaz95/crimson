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

import sys, getopt, requests, re
from collections import Counter

### OPTIONS ---
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
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

def import_wordlist(wordlist):
    '''Importing wordlist line by line into an array'''
    with open(wordlist) as wordlist:
        new_wordlist = [",".join(line.split(",")).strip() for line in wordlist.readlines()]
    return new_wordlist

def import_cookies(cookie):
    '''Importing cookies from header f.e. "Cookie: auth1=qwe; auth2=asd;" '''
    cookies = {}
    #cookie_header = cookie.split(":")[0]
    cookie_values = cookie.split(":")[1].split(";")[:-1]
    for q in cookie_values:
        cookies.update(dict([q.lstrip().split("=")]))
    return cookies

def combine_wordlists(wordlist1,wordlist2):
    '''Join strings one by one from array1 with array2'''
    new_wordlist = []
    for word1 in wordlist1:
        for word2 in wordlist2:
            new_wordlist.append(word1+word2)
    return new_wordlist

def check_backup_file(wordlist1,wordlist2,cookies,headers):
    '''Combine urls with extension wordlist and check for backup files'''
    s = requests.Session()
    s.cookies.update(cookies)
    s.headers.update(headers)
    # KARMAZ - finished here, validates  r1:r2
    print wordlist2[0]

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
try:
    urls = import_wordlist(list_of_urls)
    extensions = import_wordlist(list_of_extensions)
    cookies = import_cookies(cookies)
    backups = combine_wordlists(urls,extensions)
    check_backup_file(urls,backups,cookies,headers)
except:
    helper()
