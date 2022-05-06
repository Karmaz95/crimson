#coding: utf-8
#
### CREATED BY KARMAZ
#
#
### TO DO:
#
### FUNCTIONS:
# 1. Gather SIDs.
# 2. Measure SID generation delay.
#
#
#### WORKFLOW
# 1. "Copy as python Request" in Burp Suitre.
# 2. Paste in login_req
#   - If there is multiple steps to generate SID use get_cookie.
#   - Else do not use this function and delete lines [1-2].
# 3. python3 SID_collector.py
# 4. Copy tokens to Burp Sequencer.
#
###

import requests
import sys
from time import sleep
from urllib3.exceptions import InsecureRequestWarning
from datetime import datetime
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
proxies = {
        "http" : "http://127.0.0.1:8080",
        "https": "http://127.0.0.1:8080",
}

def login_req(proxies):
    url = "URL" # CHANGE
    headers = {}  # CHANGE
    data = {"LOGIN": "admin", "PASS":"password123"} # CHANGE
    r = requests.post(url, headers=headers, data=data, proxies=proxies, verify=False)
    init_cookie = r.cookies["SID_NAME"] # CHANGE
    return init_cookie


def get_cookie(cookie,proxies):
    url = "URL" # CHANGE
    cookies = {"SID_NAME": cookie} # CHANGE
    headers = {} # CHANGE
    r = requests.get(url, headers=headers, cookies=cookies, proxies=proxies, verify=False)
    new_cookie = r.cookies["SID_NAME"]  # CHANGE
    return new_cookie


sid = []
i = 1
start = datetime.now()
sid.append(login_req(proxies))
print("Start time: " + str(start))
print("First cookie:\n" + sid[0])
while(i<100):
    c = login_req(proxies)
    now = datetime.now()

    if c != sid[i-1]:
        sid.append(c)
        i+=1
        print(c)
        print("Cookie delay: " +str(now-start))
        start = datetime.now()

    c = get_cookie(sid[i-1],proxies)
    now = datetime.now()

    if c != sid[i-1]:
        sid.append(c)
        print(c)
        i+=1
        print("Cookie delay: " + str(now-start))
        start = datetime.now()
   # sleep(30) # CHANGEs

with open("tokens.txt", "w") as f:
    for e in sid:
        f.write(e)