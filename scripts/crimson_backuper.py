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
short_options = "w:h:"
long_options = ["wordlist", "headers"]
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

def import_headers(headers):
    headers = {}
    with open(wordlist) as wordlist:
        new_wordlist = [",".join(line.split(",")).strip() for line in wordlist.readlines()]
    urls.update({"URLS":new_wordlist})
    return urls



### OPTIONS ---
for current_argument, current_value in arguments:
    if current_argument in ("-w", "--wordlist"):
        list_of_urls = current_value
    elif current_argument in ("-h", "--headers"):
        list_of_headers = current_value

### MAIN
try:
    urls = import_wordlist(list_of_urls)
    print(urls)
except:
    helper()
