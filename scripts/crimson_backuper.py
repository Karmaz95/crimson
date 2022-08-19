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
#
# USAGE EXAMPLE:
#   python crimson_backuper.py -w urls.txt -c "Cookie: auth1=qwe; auth2=asd;" -H "asd=1" -H "qwe=2" -e BCK_EXT
###

import sys, getopt, requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from tqdm import tqdm

### OPTIONS ---
argument_list = sys.argv[1:]
short_options = "w:c:H:e:o:h"
long_options = ["wordlist", "cookies", "header", "extensions", "output", "help"]
try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    print(err)
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
    print("\nUSAGE: python crimson_backuper.py -w [wordlist_with_urls] -H [headers] -c [Cookie: a=1;] -h [show help]")

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

def combine_wordlists(wordlist1, wordlist2):
    '''Join strings one by one from array1 with array2'''
    return [w1 + w2 for w1 in wordlist1 for w2 in wordlist2]

def check_backup_file(urls, extensions, cookies, headers):
    '''Combine urls with extension wordlist and check for backup files'''
    backups_list = []
    print("\033[0;31m [+]\033[0m BACKUPER PROGRESS")
    s = requests.Session()
    s.cookies.update(cookies)
    s.headers.update(headers)
    for url in tqdm(urls):
        try:
            r1 = s.get(url, allow_redirects=True, verify=False, timeout=2)
        except KeyboardInterrupt:
            sys.exit()
        except:
            pass
        for ext in extensions:
            backup = url + ext
            try:
                r2 = s.get(backup, allow_redirects=True, verify=False, timeout=2)
                # Check if r2 is not permanently redirected, if not send r1.
                # If status code of r2 is equal 200 step into next check.
                # If Content-Length or the r2 is not the same as r1 step ino next check.
                # If there are no reflection, the backup file has been found, either way there is a path/host reflection - check for xss.
                if not r2.is_permanent_redirect and r2.status_code == 200 and r2.content != r1.content:
                    if r2.url not in r2.text:
                        backups_list.append("[+] BACKUP FILE FOUND AT: " + r2.url)
                    else:
                        backups_list.append("[+] REFLECTION FOUND AT: " + r2.ulr)
            except KeyboardInterrupt:
                sys.exit()
            except:
                pass
    return backups_list


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
    elif current_argument in ("-e", "--extensions"):
        list_of_extensions = current_value
    elif current_argument in ("-o", "--output"):
        logs_name = current_value
    elif current_argument in ("-h", "--help"):
        show_help = True

### MAIN
if __name__ == '__main__':
    if show_help:
        helper()
    else:
        urls = load_wordlist(list_of_urls)
        extensions = load_wordlist(list_of_extensions)
        if cookies:
            cookies = import_cookies(cookies)
        backups_list = check_backup_file(urls, extensions, cookies, headers)
        if logs_name is not None:
            logs_saver(backups_list, logs_name)
        else:
            for backup in backups_list:
                print(backup.rstrip())
