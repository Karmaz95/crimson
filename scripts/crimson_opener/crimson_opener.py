#coding: utf-8
#
### CREATED BY KARMAZ
#
#
### TO DO:
# 1. ADD AUTHORIZATION BEARER
# 2. ADD -P [manual payloads] 
### FUNCTIONS:
#
# 1. OPEN URLS IN FIREFOX FOR MANUAL TESTING
# 2. PROXY THROUGH BURP - turn of proxy in firefox
# 3. AUTHORIZED REQUESTS - login in other tab in Firefox on the valid account and start the opener.
#
#### WORKFLOW
# 1. Create a "manual_payloads.txt" wordlist with payloads to use and place it in the same directory.
# 2. Start the ./crimson_opener.py  -u -l -o
# 3. Open single URL                -u https://url/FUZZ 
# 4. Open wordlist(with fuzzing)    -l [lists_with_urls/FUZZ] 
# 5. Open wordlist(without fuzzing) -o [list_with_urls]
# F.e: crimson_opener.py -u https://www.example.com/FUZZ
###

import webbrowser, sys, time, getopt

### OPTIONS ---
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
short_options = "hu:l:o:"
long_options = ["help", "url", "list", "open"]
try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
        sys.exit(2)
### --- (They will be iterated at the bottom of the screen ---

### Wordlist to use
list_of_payloads = 'manual_payloads.txt'


def open_in_webrowser(url):
    # only for windows
    #webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
    webbrowser.get('firefox').open_new_tab(url)

def loop_over_file(list_of_payloads):
    print("OPENING:")
    i=0
    with open(list_of_payloads) as payloads:
        for payload in payloads:
            try:
                i+=1
                open_in_webrowser((url.rstrip()).replace("FUZZ",payload.rstrip()))
                print("ID: " + str(i) + " - URL: " + url.rstrip().replace("FUZZ",payload.rstrip()))
                ### ADJUST AS MUCH AS YOU WANT - depends on the internet connection
                time.sleep(0.2)
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                pass

def just_open(urls_list):
    print("OPENING:")
    i=0
    with open(urls_list) as urls:
        for url in urls:
            try:
                i+=1
                open_in_webrowser(url.rstrip())
                print("ID: " + str(i) + " - URL: " + url.rstrip())  
                time.sleep(0.2)
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                   pass
            
### OPTIONS ---
for current_argument, current_value in arguments:
    if current_argument in ("-h", "--help"):
        print("""\033[0;31m
 ██████╗██████╗ ██╗███╗   ███╗███████╗ ██████╗ ███╗   ██╗         ██████╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗ 
██╔════╝██╔══██╗██║████╗ ████║██╔════╝██╔═══██╗████╗  ██║        ██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██╔══██╗
██║     ██████╔╝██║██╔████╔██║███████╗██║   ██║██╔██╗ ██║        ██║   ██║██████╔╝█████╗  ██╔██╗ ██║█████╗  ██████╔╝
██║     ██╔══██╗██║██║╚██╔╝██║╚════██║██║   ██║██║╚██╗██║        ██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║██║██║ ╚═╝ ██║███████║╚██████╔╝██║ ╚████║███████╗╚██████╔╝██║     ███████╗██║ ╚████║███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝\033[0m""")
        print("\tEDIT manual_payloads.txt\n\tUSAGE: \tcrimson_opener.py\n\n \t\t-h --help => Show this help \n\t\t-u --url=\"http://example.com/FUZZ\" \n\t\t-l --list=list of urls\n\t\t-o --open=list of urls(without FUZZ)")
    elif current_argument in ("-u", "--url"):
        url = current_value 
        loop_over_file(list_of_payloads)
    elif current_argument in ("-l", "--list"):
        with open(str(current_value)) as urls:
            for url in urls:
                loop_over_file(list_of_payloads)
    elif current_argument in ("-o", "--open"):
        just_open(current_value)


### ---
