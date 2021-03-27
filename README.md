# Crimson

> Crimson is a tool that automates some of the Pentester or Bug Bounty Hunter tasks. It uses many open source tools, most of them are available for download from github.

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

# LIST OF UTILIZED TOOLS
> The following tools are used in "crimson". If you did not like my tool, then I encourage you to at least study the links below, they will definitely help you in your work.
* [nmap](https://github.com/nmap/nmap)
* [masscan](https://github.com/robertdavidgraham/masscan)
* [Amass](https://github.com/OWASP/Amass)
* [subfinder](https://github.com/projectdiscovery/subfinder)
* [massdns](https://github.com/blechschmidt/massdns)
* [assetfinder](https://github.com/tomnomnom/assetfinder)
* [Paramspider](https://github.com/devanshbatham/ParamSpider)
* [dnsx](https://github.com/projectdiscovery/dnsx)
* [getallurls](https://github.com/lc/gau)
* [waybackurls](https://github.com/tomnomnom/waybackurls)
* [CorsMe](https://github.com/Shivangx01b/CorsMe)
* [subjack](https://github.com/haccer/subjack)
* [gowitness](https://github.com/sensepost/gowitness)
* [wfuzz](https://github.com/xmendez/wfuzz)
* [ffuf](https://github.com/ffuf/ffuf)
* [webtech](https://github.com/ShielderSec/webtech)
* [WhatWeb](https://github.com/urbanadventurer/WhatWeb)
* [nikto](https://github.com/sullo/nikto)
* [wapiti](https://github.com/wapiti-scanner/wapiti)
* [gospider](https://github.com/jaeles-project/gospider)
* [hakrawler](https://github.com/hakluke/hakrawler)
* [galer](https://github.com/dwisiswant0/galer)
* [getJS](https://github.com/003random/getJS)
* [qsreplace](https://github.com/tomnomnom/qsreplace)
* [httpx](https://github.com/encode/httpx)
* [zile](https://github.com/xyele/zile)
* [wafw00f](https://github.com/EnableSecurity/wafw00f)
* [relative-url-extractor](https://github.com/jobertabma/relative-url-extractor)
* [XSStrike](https://github.com/s0md3v/XSStrike)
* [Smuggler](https://github.com/defparam/smuggler)
* [hbh-header-abuse-test.py](https://gist.github.com/ndavison/298d11b3a77b97c908d63a345d3c624d)
* [broken-link-checker](https://github.com/stevenvachon/broken-link-checker)
* [sqlmap](http://sqlmap.org/)
* [CRLFuzz](https://github.com/dwisiswant0/crlfuzz)
* [ysoserial](https://github.com/frohoff/ysoserial)
* [ysoserial.net](https://github.com/frohoff/ysoserial)
* [altdns](https://github.com/infosec-au/altdns)
* [jwt-tool](https://github.com/ticarpi/jwt_tool)
* [dalfox](https://github.com/hahwul/dalfox)
* [unfurl](https://github.com/tomnomnom/unfurl)
* [puredns](https://github.com/d3mondev/puredns)
* [sudomy](https://github.com/Screetsec/Sudomy)
* [anew](https://github.com/tomnomnom/anew.git)
* [SubDomainizer](https://github.com/nsonaniya2010/SubDomainizer)
* [HostHunter](https://github.com/SpiderLabs/HostHunter/)
* [fresh-resolvers](https://raw.githubusercontent.com/BonJarber/fresh-resolvers/)
* [wpscan](https://github.com/wpscanteam/wpscan)
* [WPluginScanner](https://github.com/linoskoczek/WPluginScanner)
* [quickpress](https://github.com/pownx/quickpress)
* [wpBullet](https://github.com/webarx-security/wpbullet)
* [FuzzHTTPBypass](https://github.com/carlospolop/fuzzhttpbypass)
* [sitemap-urls](https://github.com/yuriyyakym/sitemap-urls)
* [DirDar](https://github.com/M4DM0e/DirDar)
* [SecLists](https://github.com/danielmiessler/SecLists)
* [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
* [XSRFPROBE](https://github.com/0xInfection/XSRFProbe)

# LICENSE
> This program is free software: you can redistribute it and/or modify it under the terms of the [Apache license](https://choosealicense.com/licenses/apache-2.0/). Crimson and any contributions are Copyright © by Karol Mazurek 2020-2021.

<a href="https://www.buymeacoffee.com/karmaz95" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
