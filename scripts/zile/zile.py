# github.com/xyele
import os,sys,re,requests,random
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Base Variables
colors = ["red","green","yellow","blue","magenta","cyan","white"]
settings = {
    "threads":10,
    "requestTimeout":7,
    "requestUA":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
patterns = {
"slack_token": "(xox[p|b|o|a]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})",
"slack_webhook": "https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}",
"facebook_oauth": "[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].{0,30}['\"\\s][0-9a-f]{32}['\"\\s]",
"twitter_oauth": "[t|T][w|W][i|I][t|T][t|T][e|E][r|R].{0,30}['\"\\s][0-9a-zA-Z]{35,44}['\"\\s]",
"twitter_access_token": "[t|T][w|W][i|I][t|T][t|T][e|E][r|R].*[1-9][0-9]+-[0-9a-zA-Z]{40}",
"heroku_api": "[h|H][e|E][r|R][o|O][k|K][u|U].{0,30}[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}",
"mailgun_api": "key-[0-9a-zA-Z]{32}",
"mailchamp_api": "[0-9a-f]{32}-us[0-9]{1,2}",
"picatic_api": "sk_live_[0-9a-z]{32}",
"google_oauth_id": "[0-9(+-[0-9A-Za-z_]{32}.apps.googleusercontent.com",
"google_api": "AIza[0-9A-Za-z-_]{35}",
"google_captcha": "6L[0-9A-Za-z-_]{38}",
"google_oauth": "ya29\\.[0-9A-Za-z\\-_]+",
"amazon_aws_access_key_id": "AKIA[0-9A-Z]{16}",
"amazon_mws_auth_token": "amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
"amazonaws_url": "s3\\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\\.s3\\.amazonaws.com",
"facebook_access_token": "EAACEdEose0cBA[0-9A-Za-z]+",
"mailgun_api_key": "key-[0-9a-zA-Z]{32}",
"twilio_api_key": "SK[0-9a-fA-F]{32}",
"twilio_account_sid": "AC[a-zA-Z0-9_\\-]{32}",
"twilio_app_sid": "AP[a-zA-Z0-9_\\-]{32}",
"paypal_braintree_access_token": "access_token\\$production\\$[0-9a-z]{16}\\$[0-9a-f]{32}",
"square_oauth_secret": "sq0csp-[ 0-9A-Za-z\\-_]{43}",
"square_access_token": "sqOatp-[0-9A-Za-z\\-_]{22}",
"stripe_standard_api": "sk_live_[0-9a-zA-Z]{24}",
"stripe_restricted_api": "rk_live_[0-9a-zA-Z]{24}",
"github_access_token": "[a-zA-Z0-9_-]*:[a-zA-Z0-9_\\-]+@github\\.com*",
"private_ssh_key": "-----BEGIN PRIVATE KEY-----[a-zA-Z0-9\\S]{100,}-----END PRIVATE KEY-----",
"private_rsa_key": "-----BEGIN RSA PRIVATE KEY-----[a-zA-Z0-9\\S]{100,}-----END RSA PRIVATE KEY-----",
"gpg_private_key_block": "-----BEGIN PGP PRIVATE KEY BLOCK-----",
"generic_api_key": "[a|A][p|P][i|I][_]?[k|K][e|E][y|Y].*['|\"][0-9a-zA-Z]{32,45}['|\"]",
"generic_secret": "[s|S][e|E][c|C][r|R][e|E][t|T].*['|\"][0-9a-zA-Z]{32,45}['|\"]",
"ip_address": "(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])",
"linkFinder": "(?:\"|')(((?:[a-zA-Z]{1,10}:\/\/|\/\/)[^\"'\/]{1,}\\.[a-zA-Z]{2,}[^\"']{0,})|((?:\/|\\.\\.\/|\\.\/)[^\"'><,;| *()(%%$^\/\\\\\\[\\]][^\"'><,;|()]{1,})|([a-zA-Z0-9_\\-\/]{1,}\/[a-zA-Z0-9_\\-\/]{1,}\\.(?:[a-zA-Z]{1,4}|action)(?:[\\?|#][^\"|']{0,}|))|([a-zA-Z0-9_\\-\/]{1,}\/[a-zA-Z0-9_\\-\/]{3,}(?:[\\?|#][^\"|']{0,}|))|([a-zA-Z0-9_\\-]{1,}\\.(?:php|asp|aspx|jsp|json|action|html|js|txt|xml)(?:[\\?|#][^\"|']{0,}|)))(?:\"|')",
"password_in_url": "[a-zA-Z]{3,10}://[^/\\s:@]{3,20}:[^/\\s:@]{3,20}@.{1,100}[\"'\\s]"
}
patterns = list(zip(patterns.keys(), patterns.values()))
# Base Variables

def request(url):
    try:
        headers = {"User-Agent":settings["requestUA"]} # define http request headers as dictionary
        response = requests.get(url,timeout=settings["requestTimeout"])
        print("[+] " + url)
        return response.text
    except Exception as e:
        return ""
def printResult(x,y):
    if "--colored" in args: # if colored parameter has given as argument
        print(colored("[{}] {}".format(x,y),random.choice(colors))) # print output colored
    else:
        print("[{}] {}".format(x,y)) # print output normally
def extract(text):
    for p in patterns:
        pattern = r"[:|=|\'|\"|\s*|`|´| |,|?=|\]|\|//|/\*}]("+p[1]+r")[:|=|\'|\"|\s*|`|´| |,|?=|\]|\}|&|//|\*/]"
        res = re.findall(re.compile(pattern),text) # try to find all patterns in text
        for i in res:
            printResult(p[0],i) # call printResults for each result
def splitArgs(text):
    try:
        return text.split("\n")
    except Exception:
        return text
def fromUrl(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        extract(request("http://"+url))
        extract(request("https://"+url))
    else:
        extract(request(url))
args = list(sys.argv)[1:]
if "--file" in args: # if file parameter has given as argument
    totalFiles = []
    for root, dirs, files in os.walk("."):
        tempFiles = [os.path.join(os.getcwd(),os.path.join(root, i)[2:]) for i in files] # find every file under current directory
        totalFiles+=tempFiles # and add them to totalFiles array
    for file in totalFiles: # for each files
        try:
            read = open(file, "r", encoding='utf-8').read() # read them
            print ("[+] " + file)
            extract(read) # and call extract function
        except Exception: # if it gives error
            pass # just ignore it
elif "--request" in args: # if request parameter has given as argument
    try:
        threadPool = ThreadPoolExecutor(max_workers=settings["threads"])
        pipeText = sys.stdin.read() # read urls
        for r in splitArgs(pipeText):
            threadPool.submit(fromUrl,r)
    except UnicodeDecodeError as e:
        print("[error] binary files are not supported yet.")
elif ("--help" in args) or ("-h" in args): 
    try:
        print ("Usage:")
        print ("For getting keys from file: cat file | python3 zile.py")
        print ("For getting keys from urls/domains: cat urls | python3 zile.py --request")
        print ("For getting keys from all files under current dir:  python3 zile.py --file")
        print ("For colored output use --colored parameter")
    except Exception as e:
        print("[error] got an exception")
else: # if none of them has given
    try:
        extract(str(sys.stdin.read()))
    except UnicodeDecodeError as e:
        print("[error] binary files are not supported yet.")
