# Crimson v3

> Crimson is a tool that automates `ASSET DISCOVERY` and `VULNERABILITY SCANNING`. 

> The container is built on top of the Kali distro. 

<p align="center">
  <img src="crimson_logo.png" />
</p>

#### It consists of fourth partially interdependent modules:
* `crimson_IPcon`   - tests the single IP or range of IP addresses. Automates the process of infrastructure reconnaissance & vulnerability scanning.
* `crimson_recon`   - tests the single domain. Automate the infrastructure reconnaissance process, subdomains enumeration, and vulnerability scanning if you .
* `crimson_target`  - tests single web application. Automates the process of a single-domain reconnaissance and vulnerability scanning.
* `crimson_exploit` - automates the process of bug founding in gathered URLs.

# Installation & running
1. Pull docker container:
```
docker pull karmaz95/crimson:v3
```
2. First run of downloaded container:
```
docker run --net="host" --name crimson -it karmaz95/crimson:v3
```
3. After the first run, you can start the container by:
```
docker start crimson && docker attach crimson
```
4. If you need to copy output from the container:
```
docker cp crimson:/root/bounty/domain.name LOCAL_DEST_PATH
```


# Usage
> Commands issued inside a docker container.
## :diamonds: crimson_IPcon :diamonds:
#### :diamonds: Module zero needs `IP ADDRESS` or `list_with_ip.txt` :diamonds:
```bash
# The most optimal use:
c_0 -l ip.txt -t -u -p -k '' -v -b
```
```bash
crimson_IPcon -i IPADDRESS
        
        # Optional flags are shown below:
        -l ip.txt               # Only IPs, one per line.
        -o /root/bounty/        # The default directory is /root/bounty/$(date +%Y_%m_%d_%H_%M)
        -t                      # TCP SCAN ON (FULL RANGE) 
        -u                      # UDP SCAN ON (TOP 1000 PORTS)
        -p                      # PING SWEEP ON
        -k ''                   # 1. user enum
                                # 2. pass spraying
                                # 3. ASREPROAST (no pass)
        -v                      # VULNERABILITY SCANNING
        -b                      # BRUTE FORCE
```
* Check the [MEDIUM ARTICLE](https://karol-mazurek95.medium.com/crimson-appsec-firearm-iv-6bca2dd2e80d), which explains the `crimson_IPcon` module deeper. 

## :diamonds: crimson_recon :diamonds:
#### :diamonds: First module needs `domain name` :diamonds:
```bash
# The most optimal use (-x for domain bruteforcing):
c_1 -d "DOMAIN" -v -x
```
```bash
crimson_recon -d "domain.com" 
                   
                   # Optional flags are shown below: 
                -x # Domain brute-forcing
                -v # Virtual host discovering
                -b # Third-level subdomain brute-forcing
                -y # Proxy urls.txt and live.txt to Burp (127.0.0.1:8080)
                -j "burp.collaborator.domain" # Scan for log4j vulnerability on all URLs & live domains
```
* Check the [MEDIUM ARTICLE](https://karol-mazurek95.medium.com/crimson-appsec-firearm-i-bc242a2a910), which explains the `crimson_recon` module deeper. 

## :diamonds: crimson_target :diamonds:
####  :diamonds: Second module needs `subdomain name` :diamonds:
```bash
# The most optimal use:
c_2 -d "DOMAIN" -c "Cookie: auth1=123;" -a -v -h
# Then check urls.txt and use crimson_backuper manually on selected URLs to save time:
python "/root/tools/crimson/scripts/crimson_backuper.py" -w urls.txt -e "/root/tools/crimson/words/BCK_EXT" -c "$cookie" -o backups.txt
```
```bash
crimson_target -d "example.domain.com" 
                
                # Optional flags are shown below:
                -c "Cookie: auth1=123;"
                -j "burp.collaborator.domain" # SSRF check with quickpress
                -v # Virtual host discovering
                -a # Without this flag, you have to check for false-positives after brute-forcing manually
                -y # Proxy urls.txt and ffuf.txt to Burp (host.docker.internal:8080)
                -p # Parameter brute-forcing with Arjun (WARNING - it takes a lot of time, better use Burp Param Miner)
                -h # Test HOP-BY-HOP header deletion at the end
                -b # Check backup files on all live URLs (status code != 404) 
                   # Can take a few hours...
                -n # Use this option to skip the directory brute-forcing phase
                -k # Test HTTP inseated of HTTPS
```
* Check the [MEDIUM ARTICLE](https://karol-mazurek95.medium.com/crimson-appsec-firearm-ii-ef37cbff7ac3), which explains the `crimson_target` module deeper. 

## :diamonds: crimson_exploit :diamonds:
####  :diamonds: The third module needs two files in the current directory, `dirs.txt` and `paramst.txt`. These files are created by the `crimson_target` module in the exp directory :diamonds:
```bash
# The most optimal use - go to "exp" directory and run:
c_3 -d "BURP_DOMAIN" -i "VPS_IP"  
```

```bash
Usage: prepare two files in the current directory and use the crimson_exploit command:
    
    [*] dirs.txt - file with directories to check:
        https://target/directory1/
        https://target/directory2/
        https://target/
    
    [*] params.txt - file with parameters to check:
        https://target/example?a=1b=2
        https://target?param=asd

        # Optional flags are shown below:
        -c "Cookie: auth1=123;"
        -i 123.123.123.123 # IP for OAST testing - run the below commands on the VPS server
                              # > start: sudo tcpdump -i eth0 icmp
                              # > start: sudo python3 -m http.server 80
        -d domain.burp.com # DOMAIN for OAST testing
                              # > You can use Burp collaborator server
        -x "/root/wordlist"# Fuzzing all.txt with a given wordlist
                              # > Use '' for a default one /root/tools/crimson/words/bug
        -n                 # Turn on NUCLEI scan on all URLs
        -o                 # Test open redirection vulnerabilities on all URLs
```
#### :diamonds: Before starting third module, run the listener on your vps machine on port 80 `python -m http.server 80` and for ping payloads `tcpdump -i eth0 icmp` :diamonds:
* Check the [MEDIUM ARTICLE](https://karol-mazurek95.medium.com/crimson-appsec-firearm-iii-80f9b40e0dad), which explains the `crimson_exploit` module deeper. 

# Usage - modules description

<p align="center">
  <img src="crimson_map.jpg" />
</p>

#### :small_red_triangle_down: [] crimson_IPcon 
> Module for initial testing of the infrastructure using only IP addresses. Useful before starting Nessus.
```bash
## FUNCTIONS:
#
# 1. PING SWEEP
# 2. PORT SCANNING (TCP & UPD)
# 3. HOSTNAME ENUMERATION
# 4. ENUM4LINUX
# 5. USER ENUM - if 88 open  
# 6. AREPROAST CHECK - if 88 open
# 7. PASS SPRAYING - using username as a password with the below combinations:
#    - user
#    - USER
#    - User
#    - null (no password)
# 8. NSE SCAN
# 9. NUCLEI SCAN
# 10. SSH AUDIT
# 11. MISCONFIGURED SPF & DMARC
# 12. BRUTEFORCING (Brutespray + Kerbrute)
# 
## LISTS (output):
#
# 1.  ping_sweep.txt            - List of IP that responds to ICMP packets
# 2.    crimson_{IPADDRESS}/      - Directory with the results for the given IP ADDRESS
# 3.  *.png               - Screenshots of the main page from the nuclei scan for the web services
# 4.  discovery_scan.           - Port scan with banners (-sV)
# 5.    enum4linux.txt              - Output from enum4linux and CME
# 6.    hostnames.txt               - Hostnames from the hosthunter
# 7.    users.txt                   - Users from Kerberos user enum
# 8.    nse_scan                    - Output from nmap vulnerability scan
# 9.    nuclei.txt                  - Output from nuclei scan
# 10.   ssh-audit.txt               - Output from SSH scans
# 11.   spf_dmarc.txt               - Misconfigured spf & dmarc records
# 12.   kerbrute_valid_creds.txt    - Valid credentials from password spraying Kerberos
# 13.   kerbrute_bruteforce.txt     - Valid credentials from brute-forcing Kerberos
# 13.   brutespray-output/          - Directory with brutespray output
#
## WORKFLOW
#
# 1. Start the script
# 2. If any hostnames is resolved, you can further enumerate it using crimson_recon 
# 3. Check the output.
#
##
```


#### :small_red_triangle_down: [I] crimson_recon 
> Subdomain enumeration and vulnerability scanning for big scope like: `*.scope.com`.

```bash
## FUNCTIONS:
#
# 1. SUBDOMAIN ENUMERATION
# 2. VIRTUAL HOSTNAMES ENUMERATION
# 3. RESOLVING DOMAINS IP ADDRESSES
# 4. URLS SCRAPING
# 5. SCREENSHOTS
# 6. DOMAIN TAKEOVER CHECK
# 7  CORS CHECK
# 8. NUCLEI SCAN
# 9. LOG4J SCAN
# 10.ZONE TRANSFER CHECK  
#
## LISTS (output):
#
# 1.    live.txt            - LIVE SUBDOMAINS
# 2     status_live.txt     - STATUS CODE OF HTTP SERVICES FROM (80/443) live.txt
# 3     hosthunter.txt      - VIRTUAL HOSTNAMES
# 4     ip.txt              - IPs AND THE CORRESPONDING DOMAINS
# 5     urls.txt            - ALL CRAWLED AND LIVE URLS IN ONE FILE
# 6     status_live.txt     - HTTPS / HTTPS SUBDOMAINS STATUS CODES
# 7.    screenshots         - STATUS CODES + SCREENS
# 8.    subjack.txt         - [VULN] DOMAIN TAKEOVER ON ALL LIVE SUBDOMAINS
# 9.    cors_scan.txt       - [VULN] MISCONFIGURED CORS
# 10.   nuclei.txt          - [VULN] TEMPLATE SCAN
# 11.   log4j.txt           - [VULN] LOG4J VULN SCAN
# 12.   dnsrecon.txt        - [VULN] ZONE TRANSFER
#
## WORKFLOW
#
# 1. Start Burp Suite
#   - Create a new project - example.tld
#   - Turn off an interception
# 2. Start this script.
# 3. Check the output listed above (LISTS)
# 4. Select the single domain and start the crimson_target module
#
##
```

#### :small_red_triangle_down: [II] crimson_target
> This module covers one particular subdomain/domain for example : `www.scope.tld`.  
```bash
## FUNCTIONS:
# 1. PARSING robots.txt AND sitemap.xml
# 2. ENUMERATING WAF
# 3. ENUMERATING FRAMEWORKS & CMS
# 2. VULNERABILITY SCANNING
# 3. DOMAIN CRAWLING
# 4. DIRECTORY BRUTEFORCING
# 5. GATHERING SOURCE CODE OF JS FILES
# 6. EXTRACTING NEW ENDPOINTS FROM GATHERED SOURCE CODE
# 7. MERGING PATHS WITH DOMAIN AND PROBING FOR NEW ENDPOINTS
# 8. PROXYING LIVE RESULTS TO BURP SUITE  
# 9. PREPARING params.txt && dirs.txt FOR EXPLOIT MODULE
# 10. CHECKING POTENTIAL BACKUP FILES
# 11. TESTING HOP-BY-HOP DELETION
#
## LISTS:
#
# 1) recon.txt          - FILE WITH RECON OUTPUT
# 2) urls.txt           - FILE WITH GATHERED URLs
# 3) status_params.txt  - STATUS CODES OF urls.txt
# 4) ffuf.txt           - DIR BRUTEFORCING OUTPUT
# 5) status_dir.txt     - STATUS CODE OF ffuf.txt
# 6) exp/params.txt     - FILE PREPARED FOR crimson_exploit WITH PARAMS
# 7) exp/dirs.txt      - FILE PREPARED FOR crimson_exploit WITH DIRECTORIES
# 8) backups.txt       - POTENTIALLY BACKUP FILES 
# 9) arjun.txt         - FILE WITH BRUTEFORCED PARAMETERS
# 10) all_source_code/  - DIRECTORY WITH JS SOURCE CODES
# 11) testssl.txt       - OUTPUT FROM testssl
# 12) jwt.txt           - OUTPUT FROM jwt_tool
# 13) wp/               - DIRECTORY WITH OUTPUT FROM WordPress tools
#
## WORKFLOW
#
# 0. Start Burp - optional step
#   - Create new project - www.example.tld
#   - Turn off an interception
#   - Make active scan for proxied URLs only in scope
# 1. Start the script
#   - If you did not choose -a flag, go to /bounty/tested.domain.tld/temp and remove manually false positives entries in ferox.txt
# 2. Check the output listed above (LISTS)
# 3. Manually browse the application, click on all functionalities
# 4. Copy the whole target scope from Burp after manually browsing the target
# 5. Paste it to exp/all.txt and run crimson_exploit
#
##
```
#### :small_red_triangle_down: [III] crimson_exploit
> This module uses several tools to automate the search for certain bugs in a list of URLs.
```bash
## FUNCTIONS:
#
# 1. FUZZING PATHS IN URLS FROM dirs.txt WITH CUSTOM PAYLOADS
# 2. FUZZING PARAMS IN URLS FROM params.txt WITH CUSTOM PAYLOADS
# 3. TESTING FOR XSS
# 4. TESTING HTTP REQUEST SMUGGLING
# 5. TESTING PROTOTYPE POLLUTION
# 6. TESTING FOR BROKEN LINKS
# 7. TESTING SQLI
# 8. TESTING OUT-OF-BOUND RCE/SSRF
# 9. TESTING JAVA DESERIALIZATION
# 10. TESTING CRLF INJECTION
# 11. TESTING FOR OPEN REDIRECTION
# 12. TESTING CVES
# 13. TESTING HEADER INJECTIONS
#
## LISTS:
#
# 1. bug_params.txt         - Fuzzing output
# 2. bug_dirs.txt           - Fuzzing output
# 3. vuln_xss               - Output from XSSstrike with vulnerable URLs ready to open in browser
# 4. nuclei.txt             - Output from nuclei scanning
# 5. smuggler.txt           - Output after testing for HTTP request smuggling.
# 6. prototype-pollution.txt- Potentially vulnerable params to prototype pollution.
# 7. broken_links.txt       - Output from BLC
# 8. sqli/                  - Output from sqlmap
# 9. oob.txt                - Log after OAST  
# 10. CRLF.txt              - Output from crlfuzz
# 11. OR.txt                - Potentially vulnerable URLs to Open Redirect vulnerability
# 12. dalfox.txt            - Output from dalfox
# 13. SSTI.txt              - Output from crimson_templator with SSTI vulnerable urls.
# 14. SSTImap.txt           - Output from SSTImap
# 15. headi.txt             - Output from headi
#
## WORKFLOW
#
# 0. Start BURP - optional step
#   - Create new project - www.example.tld
#   - Turn off an interception
# 1. Start VPS listener and collaborator server
# 2. Start the script
#   - You will be asked to remove false positives from exp/dirs.txt and exp/params.txt
#   - Remove them and rerun the script as before.
# 3. Check the output listed above (LISTS)
# 4. Look for [ID] [TIME] in oob.txt and compare it to pings on your VPS / collaborator
#
##
```
# Extras
> There are some valuable tools in the scripts directory that I have written that are worth checking out.

# Contributing
> Pull requests are welcome. Please open an issue to discuss what you want to change for significant changes.

# List of utilized tools
> The following tools are used in `crimson`. I encourage you to study the links below. They will help you in your work.
> Especially check `Burp Suite extensions` because all gathered resources are proxied to Burp Suite, where they are further tested.


### OSINT:
* [spiderfoot](https://github.com/smicallef/spiderfoot.git)
* [theHarvester](https://github.com/laramies/theHarvester.git)


### IP && ports:
* [nmap](https://github.com/nmap/nmap)
* [masscan](https://github.com/robertdavidgraham/masscan)
* [rustscan](https://github.com/RustScan/RustScan.git)
* [enum4linux](https://github.com/cddmp/enum4linux-ng.git)
* [KERBRUTE](https://github.com/ropnop/kerbrute)
* [SSH-AUDIT](https://github.com/jtesta/ssh-audit)
* [BruteSpray](https://github.com/x90skysn3k/brutespray)


### Domains enumeration:
* [Amass](https://github.com/OWASP/Amass)
* [subfinder](https://github.com/projectdiscovery/subfinder)
* [massdns](https://github.com/blechschmidt/massdns)
* [dnsx](https://github.com/projectdiscovery/dnsx)
* [assetfinder](https://github.com/tomnomnom/assetfinder)
* [puredns](https://github.com/d3mondev/puredns)
* [sudomy](https://github.com/Screetsec/Sudomy)
* [altdns](https://github.com/infosec-au/altdns)
* [HostHunter](https://github.com/SpiderLabs/HostHunter/)
* [mailspoof](https://github.com/serain/mailspoof)
* [dns-wildcard-removal](https://github.com/faizal3199/dns-wildcard-removal)
* [DNSRecon](https://github.com/darkoperator/dnsrecon)


### URLs:
* [waybackurls](https://github.com/tomnomnom/waybackurls)
* [Paramspider](https://github.com/devanshbatham/ParamSpider)
* [getallurls](https://github.com/lc/gau)
* [wfuzz](https://github.com/xmendez/wfuzz)
* [ffuf](https://github.com/ffuf/ffuf)
* [feroxbuster](https://github.com/epi052/feroxbuster)
* [sitemap-urls](https://github.com/yuriyyakym/sitemap-urls)
* [gospider](https://github.com/jaeles-project/gospider)
* [hakrawler](https://github.com/hakluke/hakrawler)
* [galer](https://github.com/dwisiswant0/galer)
* [getJS](https://github.com/003random/getJS)
* [httpx](https://github.com/encode/httpx)
* [zile](https://github.com/Karmaz95/crimson/tree/master/scripts/zile)
* [crimson_backuper](https://github.com/Karmaz95/crimson/blob/master/scripts/crimson_backuper.py)
* [cariddi](https://github.com/edoardottt/cariddi)


### Target visualisation:
* [WhatWeb](https://github.com/urbanadventurer/WhatWeb)
* [gowitness](https://github.com/sensepost/gowitness)
* [wafw00f](https://github.com/EnableSecurity/wafw00f)
* [Ultimate Nmap Parser](https://github.com/shifty0g/ultimate-nmap-parser)


### Bug finding:
* [nikto](https://github.com/sullo/nikto)
* [CorsMe](https://github.com/Shivangx01b/CorsMe)
* [subjack](https://github.com/haccer/subjack)
* [XSStrike](https://github.com/s0md3v/XSStrike)
* [Smuggler](https://github.com/defparam/smuggler)
* [hbh-header-abuse-test](https://gist.github.com/ndavison/298d11b3a77b97c908d63a345d3c624d)
* [broken-link-checker](https://github.com/stevenvachon/broken-link-checker)
* [sqlmap](http://sqlmap.org/)
* [CRLFuzz](https://github.com/dwisiswant0/crlfuzz)
* [ysoserial](https://github.com/frohoff/ysoserial)
* [ysoserial.net](https://github.com/frohoff/ysoserial)
* [jwt-tool](https://github.com/ticarpi/jwt_tool)
* [dalfox](https://github.com/hahwul/dalfox)
* [testssl.sh](https://testssl.sh/)
* [crimson_templator](https://github.com/Karmaz95/crimson/blob/master/scripts/crimson_templator.py)
* [nuclei](https://github.com/projectdiscovery/nuclei)
* [headi](https://github.com/mlcsec/headi)
* [codeql](https://github.com/github/codeql-cli-binaries)
* [semgrep](https://semgrep.dev/)
* [gmapiscanner](https://github.com/ozguralp/gmapsapiscanner.git)
* [log4j-scan](https://github.com/fullhunt/log4j-scan)
* [GOAST](https://github.com/Karmaz95/crimson/tree/master/scripts/GOAST)
* [CMSEEK](https://github.com/Tuhinshubhra/CMSeeK)
* [PLUTION](https://github.com/raverrr/plution)
* [SSTIMAP](https://github.com/vladko312/SSTImap.git)
* [INQL](https://github.com/doyensec/inql.git)


### WordPress tools:
* [wpscan](https://github.com/wpscanteam/wpscan)
* [WPluginScanner](https://github.com/linoskoczek/WPluginScanner)
* [quickpress](https://github.com/pownx/quickpress)
* [wpBullet](https://github.com/webarx-security/wpbullet)


### Additional tools:
* [qsreplace](https://github.com/tomnomnom/qsreplace)
* [anew](https://github.com/tomnomnom/anew.git)
* [unfurl](https://github.com/tomnomnom/unfurl)
* [Search-That-Hash](https://github.com/HashPals/Search-That-Hash)
* [clever_ffuf](https://github.com/Karmaz95/crimson/blob/master/scripts/clever_ffuf.py)
* [crimson_opener](https://github.com/Karmaz95/crimson/tree/master/scripts/crimson_opener)
* [crimson_paramjuggler](https://github.com/Karmaz95/crimson/blob/master/scripts/crimson_paramjuggler.py)
* [tldextract](https://pypi.org/project/tldextract/)
* [PyWhat](https://github.com/bee-san/pyWhat)
* [Ciphey](https://github.com/Ciphey/Ciphey)


### Wordlists:
* [SecLists](https://github.com/danielmiessler/SecLists)
* [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
* [fresh-resolvers](https://raw.githubusercontent.com/BonJarber/fresh-resolvers/)


### Burp Suite extensions:
* [.NET Beautifier](https://github.com/portswigger/dotnet-beautifier)
* [403 Bypasser](https://github.com/portswigger/403-bypasser)
* [AWS Security Checks](https://github.com/portswigger/aws-security-checks)
* [ActiveScan++](https://github.com/portswigger/active-scan-plus-plus)
* [Anonymous Cloud, Configuration and Subdomain Takeover Scanner](https://github.com/portswigger/anonymous-cloud)
* [Asset Discovery](https://github.com/portswigger/asset-discovery)
* [Auth Analyzer](https://github.com/portswigger/auth-analyzer)
* [Backslash Powered Scanner](https://github.com/portswigger/backslash-powered-scanner)
* [Backup Finder](https://github.com/portswigger/backup-finder)
* [Burp Bounty Pro](https://burpbounty.net/)
* [CORS*, Additional CORS Checks](https://github.com/portswigger/additional-cors-checks)
* [CSP Auditor](https://github.com/portswigger/csp-auditor)
* [CSRF Scanner](https://github.com/portswigger/csrf-scanner)
* [Cloud Storage Tester](https://github.com/portswigger/cloud-storage-tester)
* [Collaborator Everywhere](https://github.com/portswigger/collaborator-everywhere)
* [Copy As Python-Requests](https://github.com/portswigger/copy-as-python-requests)
* [Cypher Injection Scanner](https://github.com/portswigger/cypher-injection-scanner)
* [Detect Dynamic JS](https://github.com/portswigger/detect-dynamic-js)
* [Error Message Checks](https://github.com/portswigger/error-message-checks)
* [ExifTool Scanner](https://github.com/portswigger/exiftool-scanner)
* [Freddy, Deserialization Bug Finder](https://github.com/portswigger/freddy-deserialization-bug-finder)
* [HTML Auditor](https://github.com/portswigger/html5-auditor)
* [HTTP Request Smuggler](https://github.com/portswigger/http-request-smuggler)
* [HTTPoxy Scanner](https://github.com/portswigger/httpoxy-scanner)
* [Hackvertor](https://github.com/portswigger/hackvertor)
* [InQL - Introspection GraphQL Scanner](https://github.com/portswigger/inql)
* [J2EEScan](https://github.com/portswigger/j2ee-scan)
* [JS Link Finder](https://github.com/portswigger/js-link-finder)
* [JS Miner](https://github.com/portswigger/js-miner)
* [JSON Web Token Attacker](https://github.com/portswigger/json-web-token-attacker)
* [JSON Web Tokens](https://github.com/portswigger/json-web-tokens)
* [JWT Editor](https://github.com/portswigger/jwt-editor)
* [JWT heartbreaker](https://github.com/wallarm/jwt-heartbreaker/releases/tag/0.1)
* [Java Deserialization Scanner](https://github.com/portswigger/java-deserialization-scanner)
* [Log4Shell Scanner](https://github.com/portswigger/log4shell-scanner)
* [meth0dman](https://github.com/portswigger/meth0d-man)
* [NGINX Alias Traversal](https://github.com/portswigger/nginx-alias-traversal)
* [NoSQLi Scanner](https://github.com/portswigger/nosqli-scanner)
* [OAuth Scan](https://github.com/portswigger/oauth-scan)
* [PHP Object Injection Check](https://github.com/portswigger/php-object-injection-check)
* [Param Miner](https://github.com/portswigger/param-miner)
* [pMDetector](https://github.com/Karmaz95/crimson/blob/master/scripts/BURP/PostMessageDetector.py)
* [Reflected Parameters](https://github.com/portswigger/reflected-parameters)
* [Retire.js](https://github.com/portswigger/retire-js)
* [SRI Check](https://github.com/portswigger/sri-check)
* [SSL Scanner](https://github.com/portswigger/ssl-scanner)
* [SameSite Reporter](https://github.com/portswigger/samesite-reporter)
* [SAML Raider](https://github.com/portswigger/saml-raider)
* [Similar Request Excluder](https://github.com/portswigger/similar-request-excluder)
* [Software Version Reporter](https://github.com/portswigger/software-version-reporter)
* [Software Vulnerability Scanner](https://github.com/portswigger/software-vulnerability-scanner)
* [Taborator](https://github.com/portswigger/taborator)
* [Turbo Intruder](https://github.com/portswigger/turbo-intruder)
* [UploadScanner](https://github.com/portswigger/upload-scanner)
* [Web Cache Deception Scanner](https://github.com/portswigger/web-cache-deception-scanner)

# LEARNING MATERIALS
> Check out the AppSec Tales series on [My Blog](https://medium.com/@karol-mazurek95/list/appsec-tales-c709435a44d0).

# HISTORY
> If you are curious how it all started:
* [Medium article](https://karol-mazurek95.medium.com/automation-of-the-reconnaissance-phase-during-web-application-penetration-testing-i-574fd9dce53e) - `crimson_recon`
* [Medium article](https://karol-mazurek95.medium.com/automation-of-the-reconnaissance-phase-during-web-application-penetration-testing-ii-4336bd4ca73b?sk=ba289442112704cd71ac4a89e994fc8c) - `crimson_target`
* [Medium article](https://karol-mazurek95.medium.com/automation-of-the-reconnaissance-phase-during-web-application-penetration-testing-iii-2823b16f38cc) - `crimson_exploit`

# LICENSE
> This program is free software: you can redistribute it and/or modify it under the terms of the [Apache license](https://choosealicense.com/licenses/apache-2.0/). Crimson and any contributions are Copyright © by Karol Mazurek 2020-2022.

# SUPPORT
> You can support the project by buying me a coffee or via [NFT](https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/63545429842149574507305116647116186975620361263604520406486432940112228647212/).

<a href="https://www.buymeacoffee.com/karmaz95" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 200px !important;" ></a>
