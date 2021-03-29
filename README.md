# Crimson

> Crimson is a tool that automates some of the Pentester or Bug Bounty Hunter tasks.  
> It uses many open source tools, most of them are available for download from github.

<p align="center">
  <img src="crimson_logo.png" />
</p>

#### It consists of three partially interdependent modules:
* crimson_recon   - automates the process of domain reconnaissance.
* crimson_target  - automates the process of urls reconnaissance.
* crimson_exploit - automates the process of bug founding.


#### :small_red_triangle_down:crimson_recon
> This module can help you if you have to test big infrastructure or you are trying to earn some bounties in *.scope.com domain. It includes many web scraping and bruteforcing tools.

#### :small_red_triangle_down:crimson_target
> This module covers one particular domain chosen by you for testing. It uses a lot of vulnerability scanners, web scrapers and bruteforcing tools.

#### :small_red_triangle_down:crimson_exploit
> This module uses a number of tools to automate the search for certain bugs in a list of urls.
# Installation
Tested on Linux Mint and Kali Linux.
```bash
git clone https://github.com/Karmaz95/crimson.git 
cd crimson
chmod +x install.sh
./install.sh
```
Add below line to your .bashrc / .zshrc etc.
```bash
export GOPATH=$HOME/go
export PATH="$HOME/bin:$HOME/.local/bin:$HOME/go/bin:$HOME/tools:$PATH"
```
Install Burp Suite
# Usage
##### :diamonds: First module needs `domain name` to work properly, f.e. `google.com` :diamonds:

```bash
./crimson_recon "domain.com"

```
* If you are interested in how this module works, I encourage you to study the source code. I tried to describe in the comments how the individual tools works. 
* Additionally, you can learn more about `crimson_recon` module by reading my article at [medium](https://karol-mazurek95.medium.com/automation-of-the-reconnaissance-phase-during-web-application-penetration-testing-i-574fd9dce53e)
 
##### :diamonds: Second module needs `subdomain name`. You can additionally put `authorization cookie` :diamonds:
```bash
./crimson_target -d "example.domain.com" -c "Cookie: auth1=123;"
```
* If you are interested in how this module works, I encourage you to study the source code. I tried to describe in the comments how the individual tools works.
* Additionally, you can learn more about `crimson_target` module by reading my article at [medium](https://karol-mazurek95.medium.com/automation-of-the-reconnaissance-phase-during-web-application-penetration-testing-ii-4336bd4ca73b?sk=ba289442112704cd71ac4a89e994fc8c)

##### :diamonds: Third module needs `subdomain name` with your `collaborator` and `vps ip`. You can additionally put `authorization cookie` :diamonds:
```bash
./crimson_exploit -D "example.domain.com" -c "Cookie: auth1=123;" -d "collaborator.com" -i "ip"
```
##### :diamonds: Before starting the script run the listener on your vps machine on port 80 :diamonds:

# Extras
> There are some useful tools in the scripts directory that I have written that are worth checking out.

# Contributing
> Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# List of utilized tools
> The following tools are used in `crimson`. I encourage you to study the links below, they will definitely help you in your work.
> Especially check `Burp Suite extensions`, because all gathered resources are proxied to Burp Suite, where they are further tested.


### :diamonds: Domains enumeration:
* [Amass](https://github.com/OWASP/Amass)
* [subfinder](https://github.com/projectdiscovery/subfinder)
* [massdns](https://github.com/blechschmidt/massdns)
* [dnsx](https://github.com/projectdiscovery/dnsx)
* [assetfinder](https://github.com/tomnomnom/assetfinder)
* [SubDomainizer](https://github.com/nsonaniya2010/SubDomainizer)
* [puredns](https://github.com/d3mondev/puredns)
* [sudomy](https://github.com/Screetsec/Sudomy)
* [altdns](https://github.com/infosec-au/altdns)
* [HostHunter](https://github.com/SpiderLabs/HostHunter/)


### :diamonds: IP && ports:
* [nmap](https://github.com/nmap/nmap)
* [masscan](https://github.com/robertdavidgraham/masscan)


### :diamonds: URLs:
* [waybackurls](https://github.com/tomnomnom/waybackurls)
* [Paramspider](https://github.com/devanshbatham/ParamSpider)
* [getallurls](https://github.com/lc/gau)
* [wfuzz](https://github.com/xmendez/wfuzz)
* [ffuf](https://github.com/ffuf/ffuf)
* [sitemap-urls](https://github.com/yuriyyakym/sitemap-urls)
* [gospider](https://github.com/jaeles-project/gospider)
* [hakrawler](https://github.com/hakluke/hakrawler)
* [galer](https://github.com/dwisiswant0/galer)
* [getJS](https://github.com/003random/getJS)
* [httpx](https://github.com/encode/httpx)
* [zile](https://github.com/xyele/zile)
* [relative-url-extractor](https://github.com/jobertabma/relative-url-extractor)
* [crimson_backuper](https://github.com/Karmaz95/crimson/blob/master/scripts/crimson_backuper.py)


### :diamonds: Target visualisation:
* [webtech](https://github.com/ShielderSec/webtech)
* [WhatWeb](https://github.com/urbanadventurer/WhatWeb)
* [gowitness](https://github.com/sensepost/gowitness)
* [wafw00f](https://github.com/EnableSecurity/wafw00f)


### :diamonds: Bug finding:
* [nikto](https://github.com/sullo/nikto)
* [wapiti](https://github.com/wapiti-scanner/wapiti)
* [CorsMe](https://github.com/Shivangx01b/CorsMe)
* [subjack](https://github.com/haccer/subjack)
* [XSRFPROBE](https://github.com/0xInfection/XSRFProbe)
* [DirDar](https://github.com/M4DM0e/DirDar)
* [XSStrike](https://github.com/s0md3v/XSStrike)
* [Smuggler](https://github.com/defparam/smuggler)
* [hbh-header-abuse-test.py](https://gist.github.com/ndavison/298d11b3a77b97c908d63a345d3c624d)
* [broken-link-checker](https://github.com/stevenvachon/broken-link-checker)
* [sqlmap](http://sqlmap.org/)
* [CRLFuzz](https://github.com/dwisiswant0/crlfuzz)
* [ysoserial](https://github.com/frohoff/ysoserial)
* [ysoserial.net](https://github.com/frohoff/ysoserial)
* [jwt-tool](https://github.com/ticarpi/jwt_tool)
* [dalfox](https://github.com/hahwul/dalfox)
* [testssl.sh](https://testssl.sh/)
* [crimson_deserializator](https://github.com/Karmaz95/crimson/blob/master/scripts/crimson_deserializator.py)
* [crimson_oobtester](https://github.com/Karmaz95/crimson/blob/master/scripts/crimson_oobtester.py)
* [crimson_rewriter](https://github.com/Karmaz95/crimson/blob/master/scripts/crimson_rewriter.py)
* [crimson_templator](https://github.com/Karmaz95/crimson/blob/master/scripts/crimson_templator.py)


### :diamonds: WordPress tools:
* [wpscan](https://github.com/wpscanteam/wpscan)
* [WPluginScanner](https://github.com/linoskoczek/WPluginScanner)
* [quickpress](https://github.com/pownx/quickpress)
* [wpBullet](https://github.com/webarx-security/wpbullet)


### :diamonds: Additional tools:
* [qsreplace](https://github.com/tomnomnom/qsreplace)
* [anew](https://github.com/tomnomnom/anew.git)
* [unfurl](https://github.com/tomnomnom/unfurl)
* [clever_ffuf](https://github.com/Karmaz95/crimson/blob/master/scripts/clever_ffuf.py)
* [crimson_opener](https://github.com/Karmaz95/crimson/tree/master/scripts/crimson_opener)
* [crimson_paramjuggler](https://github.com/Karmaz95/crimson/blob/master/scripts/crimson_paramjuggler.py)


### :diamonds: Wordlists:
* [SecLists](https://github.com/danielmiessler/SecLists)
* [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
* [fresh-resolvers](https://raw.githubusercontent.com/BonJarber/fresh-resolvers/)


### :diamonds: Burp Suite extensions:
* [ActiveScan++](https://portswigger.net/bappstore/3123d5b5f25c4128894d97ea1acc4976)
* [UploadScanner](https://portswigger.net/bappstore/b2244cbb6953442cb3c82fa0a0d908fa)
* [Wayback Machine](https://portswigger.net/bappstore/5c7c516c690345c19fbf55b2b2ebeb76)
* [Taborator](https://portswigger.net/bappstore/c9c37e424a744aa08866652f63ee9e0f)
* [Software Version Reporter](https://portswigger.net/bappstore/ae62baff8fa24150991bad5eaf6d4d38)
* [Software Vulnerability Scanner](https://portswigger.net/bappstore/c9fb79369b56407792a7104e3c4352fb)
* [Turbo Intruder](https://portswigger.net/bappstore/9abaa233088242e8be252cd4ff534988)
* [SameSite Reporter](https://portswigger.net/bappstore/ea1aa264b86d424ba35760d7e24c9e60)
* [Same Origin Method Execution](https://portswigger.net/bappstore/9fea3ce4e79d450a9a15d05a79f9d349)
* [Retire.js](https://portswigger.net/bappstore/36238b534a78494db9bf2d03f112265c)
* [Reflected Parameters](https://portswigger.net/bappstore/8e8f6bb313db46ba9e0a7539d3726651)
* [PHP Object Injection Check](https://portswigger.net/bappstore/24dab228311049d89a27a4d721e17ef7)
* [NoSQLi Scanner](https://portswigger.net/bappstore/605a859f0a814f0cbbdce92bc64233b4)
* [NGINX Alias Traversal](https://portswigger.net/bappstore/a5fdd2cdffa6410eb530de5a4c294d3a)
* [JS Link Finder](https://portswigger.net/bappstore/0e61c786db0c4ac787a08c4516d52ccf)
* [Java Deserialization Scanner](https://portswigger.net/bappstore/228336544ebe4e68824b5146dbbd93ae)
* [J2EEScan](https://portswigger.net/bappstore/7ec6d429fed04cdcb6243d8ba7358880)
* [Logger++](https://portswigger.net/bappstore/470b7057b86f41c396a97903377f3d81)
* [Freddy, Deserialization Bug Finder](https://portswigger.net/bappstore/ae1cce0c6d6c47528b4af35faebc3ab3)
* [Error Message Checks](https://portswigger.net/bappstore/4f01db4b668c4126a68e4673df796f0f)
* [Detect Dynamic JS](https://portswigger.net/bappstore/4a657674ebe3410b92280613aa512304)
* [CSP-Bypass](https://portswigger.net/bappstore/b113bdc1390647b092cb527c0b95116d)
* [CSRF Scanner](https://portswigger.net/bappstore/60f172f27a9b49a1b538ed414f9f27c3)
* [Collaborator Everywhere](https://portswigger.net/bappstore/2495f6fb364d48c3b6c984e226c02968)
* [Cloud Storage Tester](https://portswigger.net/bappstore/04adbe101f544c88b2497a9a25ffaab4)
* [Backslash Powered Scanner](https://portswigger.net/bappstore/9cff8c55432a45808432e26dbb2b41d8)
* [AWS Security Checks](https://portswigger.net/bappstore/f078b9254eab40dc8c562177de3d3b2d)
* [Anonymous Cloud, Configuration and Subdomain Takeover Scanner](https://portswigger.net/bappstore/ea60f107b25d44ddb59c1aee3786c6a1)
* [Additional Scanner Checks](https://portswigger.net/bappstore/a158fd3fc9394253be3aa0bc4c181d1f)
* [Param Miner](https://portswigger.net/bappstore/17d2949a985c4b7ca092728dba871943)
* [HTTP Request Smuggler](https://portswigger.net/bappstore/aaaa60ef945341e8a450217a54a11646)
* [Auth Analyzer](https://portswigger.net/bappstore/7db49799266c4f85866f54d9eab82c89)
* [Web Cache Deception Scanner](https://portswigger.net/bappstore/7c1ca94a61474d9e897d307c858d52f0)
* [Attack Surface Detector](https://portswigger.net/bappstore/47027b96525d4353aea5844781894fb1)
* [Autowasp](https://portswigger.net/bappstore/b89968942a3e4cab916b6c761beb2003)
* [InQL - Introspection GraphQL Scanner](https://portswigger.net/bappstore/296e9a0730384be4b2fffef7b4e19b1f)
* [ViewState Editor](https://portswigger.net/bappstore/ba17d9fb487448b48368c22cb70048dc)
* [Paramalyzer](https://portswigger.net/bappstore/0ac13c45adff4e31a3ca8dc76dd6286c)
* [ExifTool Scanner](https://portswigger.net/bappstore/858352a27e6e4a6caa802e61fdeb7dd4)
* [Similar Request Excluder](https://portswigger.net/bappstore/9ecd51851baf4ae6b69c6a951257387a)
* [.NET Beautifier](https://portswigger.net/bappstore/e2a137ad44984ccb908375fa5b2c618d)


# LICENSE
> This program is free software: you can redistribute it and/or modify it under the terms of the [Apache license](https://choosealicense.com/licenses/apache-2.0/). Crimson and any contributions are Copyright © by Karol Mazurek 2020-2021.

<a href="https://www.buymeacoffee.com/karmaz95" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 200px !important;" ></a>
