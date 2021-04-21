#!/bin/bash
sudo rm /etc/apt/preferences.d/nosnap.pref
sudo apt update -y
sudo apt dist-upgrade -y
sudo apt install ruby ruby-dev libpcap-dev libldns-dev golang python sqlmap mono-complete wine winetricks git snapd nmap wfuzz dnsrecon python3 python3-dnspython pv xed ldnsutils jq testssl.sh whatweb masscan wafw00f gobuster -y
sudo gem install bundler json mongo
sudo apt install python3-pip nodejs -y
sudo add-apt-repository universe
sudo apt update -y
sudo apt install python2 build-essential -y
sudo apt install npm -y
sudo python2 get-pip.py
mkdir $HOME/bounty
mkdir -p $HOME/tools/CRIMSON/
cp -r * $HOME/tools/CRIMSON/
cd $HOME/tools
### WAPITI
python3 -m pip install wapiti3
sudo apt install wapiti -y
### AMASS
sudo snap install amass
### MASSDNS
git clone https://github.com/blechschmidt/massdns.git
cd massdns
make
sudo cp bin/massdns /usr/bin/massdns
cd ..
### GOOGLE CHROME
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update -y
sudo apt install -y google-chrome-stable
### BROKEN LINK CHECKER
sudo npm install broken-link-checker -g
### CMSEEK
git clone https://github.com/Tuhinshubhra/CMSeeK.git
cd CMSeeK
python3 -m pip install -r requirements.txt
cd ..
### FFUF INSTALL
go get -u github.com/ffuf/ffuf
### SUBFINDER
GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder
### PARAMSPIDER
git clone https://github.com/devanshbatham/ParamSpider
cd ParamSpider
python3 -m pip install -r requirements.txt
cd ..
### ASSETFINDER
go get -u github.com/tomnomnom/assetfinder
### GOWITNESS
go get -u github.com/sensepost/gowitness
### HTTPROBE
go get -u github.com/tomnomnom/httprobe
### CORSME
go get -u -v github.com/shivangx01b/CorsMe
### SUBJACK
go get github.com/haccer/subjack
### HAKRAWLER
go get github.com/hakluke/hakrawler
### ARJUN
git clone https://github.com/s0md3v/Arjun.git
cd Arjun
python3 setup.py install
cd ..
### SMUGGLER
git clone https://github.com/defparam/smuggler
### GOSPIDER
go get -u github.com/jaeles-project/gospider
### XSSTRIKE
git clone https://github.com/s0md3v/XSStrike.git
cd XSStrike
python3 -m pip install -r requirements.txt
cd ..
### DALFOX
GO111MODULE=on go get -v github.com/hahwul/dalfox/v2
### WAYBACKURLS
go get github.com/tomnomnom/waybackurls
### UNFURL
go get -u github.com/tomnomnom/unfurl
### QSREPLACE
go get -u github.com/tomnomnom/qsreplace
### DNSX
GO111MODULE=on go get -v github.com/projectdiscovery/dnsx/cmd/dnsx
### JSBEAUTIFIER
pip install jsbeautifier
### GETJS
go get github.com/003random/getJS
### LINKFINDER
git clone https://github.com/GerbenJavado/LinkFinder.git
cd LinkFinder
python setup.py install
python3 -m pip install -r requirements.txt
cd ..
### CRLFUZZ
GO111MODULE=on go get -v github.com/dwisiswant0/crlfuzz/cmd/crlfuzz
### WEBTECH
pip install webtech
### GAU
GO111MODULE=on go get -u -v github.com/lc/gau
mv $HOME/go/bin/gau $HOME/go/bin/get-all-urls
### GALLER
GO111MODULE=on go get github.com/dwisiswant0/galer
### HTTPX
GO111MODULE=on go get -v github.com/projectdiscovery/httpx/cmd/httpx
### FEROXBUSTER
curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/master/install-nix.sh | bash
### TLDEXTRACT
pip install tldextract
pip2 install tldextract
### NIKTO 
git clone https://github.com/sullo/nikto.git
### DOTNET48
winetricks dotnet48
### YSOSERIAL
mkdir ysoserial
wget https://jitpack.io/com/github/frohoff/ysoserial/master-SNAPSHOT/ysoserial-master-SNAPSHOT.jar -O ysoserial/ysoserial.jar
### SEARCH THAT HASH
python3 -m pip install search-that-hash
### ALTDNS
pip install py-altdns shodan
### JWT-TOOL
git clone https://github.com/ticarpi/jwt_tool
python3 -m pip install termcolor cprint pycryptodomex requests
### PUREDNS
git clone https://github.com/d3mondev/puredns.git
### SUDOMY
git clone --recursive https://github.com/screetsec/Sudomy.git
python3 -m pip install -r Sudomy/requirements.txt
### SUBDOMAINIZER
git clone https://github.com/nsonaniya2010/SubDomainizer.git
python3 -m pip install -r SubDomainizer/requirements.txt
### HOSTHUNTER
git clone https://github.com/SpiderLabs/HostHunter.git
python3 -m pip install -r HostHunter/requirements.txt
### ANEW
go get -u github.com/tomnomnom/anew
### WPSCAN
gem install wpscan
### QUICKPRESS
go get github.com/fatih/color
git clone https://github.com/pownx/quickpress.git
cd quickpress
go build -o quickpress
cd ..
### WPLUGINSCANNER
git clone --depth 1 https://github.com/linoskoczek/WPluginScanner
cd WPluginScanner
python3 crawlpopular.py
python3 crawlall.py
cd ..
### WPBULLET
git clone https://github.com/webarx-security/wpbullet wpbullet
pip install -r wpbullet/requirements.txt
### SITEMAP-URLS
git clone https://github.com/yuriyyakym/sitemap-urls.git
### CRIMSON LIBS
pip install future tqdm IPy
### DIRDAR
go get -u github.com/m4dm0e/dirdar
### HBH-HEADER-ABUSE
git clone https://gist.github.com/298d11b3a77b97c908d63a345d3c624d.git hop-by-hop/
### SHCHECK
python3 -m pip install shcheck
### PROTOTYPE POLLUTION
go get github.com/TwinProduction/go-color
go get -u github.com/chromedp/chromedp
cp 
### NUCLEI
GO111MODULE=on go get -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei
nuclei -update-templates
### DNSPROBE
GO111MODULE=on go get -v github.com/projectdiscovery/dnsprobe
### WEBANALYZE
go get -v -u github.com/rverton/webanalyze/cmd/webanalyze
### CF-CHECK
go get -u github.com/dwisiswant0/cf-check
### HEADI
go get github.com/mlcsec/headi
### NAABU
GO111MODULE=on go get -v github.com/projectdiscovery/naabu/v2/cmd/naabu
### CODEQL
cd $HOME/tools
wget https://github.com/github/codeql-cli-binaries/releases/download/v2.5.1/codeql-linux64.zip
unzip codeql-linux64.zip
rm codeql-linux64.zip
### METASPLOIT
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall  
chmod 755 msfinstall  
sudo ./msfinstall