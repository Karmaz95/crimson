#!/bin/bash
sudo rm /etc/apt/preferences.d/nosnap.pref
sudo apt update -y
sudo apt dist-upgrade -y
sudo apt install ruby ruby-dev libldns-dev golang python sqlmap mono-complete wine winetricks git snapd nmap wfuzz dnsrecon python3 python3-dnspython pv scite ldnsutils -y
sudo gem install bundler json mongo
sudo apt install python3-pip 
sudo add-apt-repository universe
sudo apt update
sudo apt install python2
curl https://bootstrap.pypa.io/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py
mkdir $HOME/bounty
mkdir -p $HOME/tools/CRIMSON/
cp -r * $HOME/tools/CRIMSON/
cd $HOME/tools
### AMASS
sudo snap install amass
### FFUF INSTALL
go get -u github.com/ffuf/ffuf
### SUBFINDER
GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder
### PARAMSPIDER
git clone https://github.com/devanshbatham/ParamSpider
cd ParamSpider
pip3 install -r requirements.txt
cd ..
### MASSDNS
git clone https://github.com/blechschmidt/massdns.git
cd massdns
make
sudo cp bin/massdns /usr/bin/massdns
cd ..
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
pip install -r requirements.txt
cd ..
### XSSTRON
git clone https://github.com/RenwaX23/XSSTRON
cd XSSTRON
npm install
npm start
### DALFOX
GO111MODULE=on go get -v github.com/hahwul/dalfox/v2
### WAYBACKURLS
go get github.com/tomnomnom/waybackurls
### UNFURL
go get -u github.com/tomnomnom/unfurl
### QSREPLACE
go get -u github.com/tomnomnom/qsreplace
### DIRHUNT
sudo pip3 install dirhunt
### wafw00f
sudo apt install wafw00f -y
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
pip3 install -r requirements.txt
cd ..
### TPLMAP 
git clone https://github.com/epinna/tplmap.git
cd tplmap
pip install -r requirements.txt
cd ..
### CRLFUZZ
GO111MODULE=on go get -v github.com/dwisiswant0/crlfuzz/cmd/crlfuzz
### WAPITI
https://github.com/wapiti-scanner/wapiti.git
cd wapiti 
sudo python setup.py install
pip install wapiti3
cd ..
### WHATWEB
git clone https://github.com/urbanadventurer/WhatWeb.git
cd WhatWeb
make install
bundle install
cd ..
### WEBTECH
pip install webtech
### SEARCHSPLOIT
git clone https://github.com/offensive-security/exploit-database.git
mv exploit-database exploitdb
### GALLER
GO111MODULE=on go get github.com/dwisiswant0/galer
### GOOGLE CHROME
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update -y
sudo apt install -y google-chrome-stable
### HTTPX
GO111MODULE=on go get -v github.com/projectdiscovery/httpx/cmd/httpx
### BROKEN LINK CHECKER
sudo npm install broken-link-checker -g
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
pip3 install search-that-hash
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
pip3 install -r SubDomainizer/requirements.txt
### HOSTHUNTER
git clone https://github.com/SpiderLabs/HostHunter.git
pip3 install -r HostHunter/requirements.txt
### ANEW
go get -u github.com/tomnomnom/anew
### WPSCAN
gem install wpscan
### METASPLOIT
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall  
chmod 755 msfinstall  
sudo ./msfinstall
