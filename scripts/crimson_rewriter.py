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

import requests

def rewriter_check(list_of_urls):
    original = []
    rewrite = []
    print("[*] CURENTLY TESTING")
    with open (list_of_urls) as urls:
        for url in urls:
            try:
                print(url.rstrip())
                r1 = requests.get(url.rstrip())
                r2 = requests.get(url.rstrip(), headers={'X-Original-Url':'/doesnotextist123'})
                r3 = requests.get(url.rstrip(), headers={'X-Rewrite-Url':'/doesnotexist321'})
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

# MAIN LOOP
list_of_urls = "all.txt"
rewriter_check(list_of_urls)
