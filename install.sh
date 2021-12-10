#!/bin/bash
sudo rm /etc/apt/preferences.d/nosnap.pref
sudo apt update -y
sudo apt dist-upgrade -y
sudo apt install composer ruby ruby-dev libpcap-dev libldns-dev golang python sqlmap mono-complete wine winetricks git snapd nmap wfuzz dnsrecon python3 python3-dnspython pv ldnsutils jq testssl.sh whatweb masscan wafw00f gobuster -y
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
### AMASS
sudo snap install amass
### MASSDNS
git clone https://github.com/blechschmidt/massdns.git
cd massdns
make
make install
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
python3 -m pip install arjun
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
GO111MODULE=on go install github.com/d3mondev/puredns/v2@latest
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
### CODEQL
cd $HOME/tools
#wget https://github.com/github/codeql-cli-binaries/releases/download/v2.5.1/codeql-linux64.zip
wget https://github.com/github/codeql-cli-binaries/releases/download/v2.6.3/codeql-linux64.zip
unzip codeql-linux64.zip
rm codeql-linux64.zip
### SEMGREP
python3 -m pip install semgrep
### RUST
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
### RUSTSCAN
git clone https://github.com/RustScan/RustScan.git
cd RustScan
cargo build --release
cd $HOME/.local/bin
ln -s $HOME/tools/RustScan/target/release/rustscan rustscan
cd $HOME/tools
### EXTRACT.RB
git clone https://github.com/jobertabma/relative-url-extractor.git
### GMAPISCANNER
git clone https://github.com/ozguralp/gmapsapiscanner.git
### PYWHAT
pip3 install pywhat
### CIPHEY
python3 -m pip install ciphey --upgrade
### cswsh-scanner
go get -v -u github.com/ambalabanov/cswsh-scanner/...
### METASPLOIT
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall  
chmod 755 msfinstall  
sudo ./msfinstall

### Dockerizing
sudo docker -it --name crimson karmaz95/crimson:v0
docker container commit crimson karmaz95/crimson:v2
docker push crimson karmaz95/crimson:v2

### Crimson 2.0
cd && apt update -y && apt install -y vim git testssl.sh bsdmainutils && echo -e "export PATH=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/go/bin:/root/go/bin:$HOME/tools/codeql:/root/tools/CRIMSON/:\"" >> $HOME/.bashrc && echo -e "alias python=\"python2\"" >> .bashrc && source $HOME/.bashrc && apt install python2 build-essential nmap dnsutils jq wget curl -y && mkdir -p "$HOME"/tools/CRIMSON/scripts/codeql/ $HOME/tools/CRIMSON/ $HOME/bounty $HOME/tools/CRIMSON/words/exp $HOME/tools/CRIMSON/scripts/zile $HOME/tools/CRIMSON/scripts/GOAST && cd tools && git clone https://github.com/Karmaz95/crimson.git && cd crimson && python2 get-pip.py && cd $HOME/tools && pip install tldextract tqdm && wget https://golang.org/dl/go1.17.1.linux-amd64.tar.gz && tar -C /usr/local -xzf go1.17.1.linux-amd64.tar.gz && rm -rf go1.17.1.linux-amd64.tar.gz && apt install python3 python3-pip -y && python3 -m pip install py-altdns==1.0.2 shodan detect-secrets arjun && git clone --recursive https://github.com/screetsec/Sudomy.git && python3 -m pip install -r Sudomy/requirements.txt && git clone https://github.com/devanshbatham/ParamSpider && python3 -m pip install -r ParamSpider/requirements.txt && git clone https://github.com/blechschmidt/massdns.git && cd massdns && make && make install && cd .. && GO111MODULE=on go install github.com/d3mondev/puredns/v2@latest && go install github.com/tomnomnom/anew@latest && go install  github.com/OWASP/Amass/v3/...@latest && go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest && go install github.com/tomnomnom/assetfinder@latest && GO111MODULE=on go install github.com/lc/gau@latest && go install github.com/tomnomnom/unfurl@latest && go install github.com/tomnomnom/waybackurls@latest && go install github.com/tomnomnom/qsreplace@latest && GO111MODULE=on go install github.com/projectdiscovery/httpx/cmd/httpx@latest && go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest && go install github.com/sensepost/gowitness@latest && go install github.com/shivangx01b/CorsMe@latest && go install github.com/haccer/subjack@latest && GO111MODULE=on go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest && GO111MODULE=on go install github.com/jaeles-project/gospider@latest && go install github.com/hakluke/hakrawler@latest && go install github.com/dwisiswant0/galer@latest && go install github.com/ffuf/ffuf@latest && go install github.com/003random/getJS@latest && go install github.com/hahwul/dalfox/v2@latest && cp -r "$HOME"/tools/crimson/scripts/GOAST/GOAST.go "$HOME"/tools/CRIMSON/scripts/GOAST/ && cp "$HOME"/tools/crimson/words/dns "$HOME"/tools/CRIMSON/words/ && cp "$HOME"/tools/crimson/words/dns-altdns.txt "$HOME"/tools/CRIMSON/words/dns-altdns.txt && cp "$HOME"/tools/crimson/words/blank "$HOME"/tools/CRIMSON/words/blank && cp "$HOME"/tools/crimson/crimson_recon "$HOME"/tools/CRIMSON/crimson_recon && cp "$HOME"/tools/crimson/crimson_target "$HOME"/tools/CRIMSON/ && cp "$HOME"/tools/crimson/crimson_exploit "$HOME"/tools/CRIMSON/&& cp "$HOME"/tools/crimson/words/dir "$HOME"/tools/CRIMSON/words/ && cp "$HOME"/tools/crimson/scripts/clever_ffuf.py "$HOME"/tools/CRIMSON/scripts/ && cp "$HOME"/tools/crimson/scripts/zile/zile.py "$HOME"/tools/CRIMSON/scripts/zile/zile.py && cp "$HOME"/tools/crimson/scripts/crimson_backuper.py "$HOME"/tools/CRIMSON/scripts/crimson_backuper.py && cp "$HOME"/tools/crimson/words/exp/OOB "$HOME"/tools/CRIMSON/words/exp/OOB && git clone https://github.com/nsonaniya2010/SubDomainizer.git && python3 -m pip install -r SubDomainizer/requirements.txt && git clone https://github.com/SpiderLabs/HostHunter.git && python3 -m pip install -r HostHunter/requirements.txt && git clone https://github.com/s0md3v/XSStrike.git && python3 -m pip install -r XSStrike/requirements.txt && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh && source $HOME/.cargo/env && git clone https://github.com/RustScan/RustScan.git && cd RustScan && cargo build --release && cd /usr/local/bin/ && ln -s $HOME/tools/RustScan/target/release/rustscan rustscan && cd $HOME/tools && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub |  apt-key add - && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" |  tee /etc/apt/sources.list.d/google-chrome.list &&  apt update -y && apt install -y google-chrome-stable wfuzz dnsrecon ldnsutils jsbeautifier wafw00f whatweb && git clone https://github.com/Tuhinshubhra/CMSeeK.git && git clone https://github.com/sullo/nikto && cd /usr/local/bin/ && ln -s $HOME/tools/nikto/program/nikto.pl nikto && curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/master/install-nix.sh | bash && cd $HOME/tools && mkdir -p $HOME/tools/ysoserial && apt -y install default-jdk ruby-dev && go install -v github.com/dwisiswant0/crlfuzz/cmd/crlfuzz@latest && cp $HOME/tools/crimson/scripts/GOAST/ysoserial.jar $HOME/tools/CRIMSON/scripts/GOAST/ysoserial.jar && cp $HOME/tools/crimson/scripts/crimson_deserializator.py $HOME/tools/CRIMSON/scripts/ && cp "$HOME"/tools/crimson/scripts/crimson_paramjuggler.py "$HOME"/tools/CRIMSON/scripts/crimson_paramjuggler.py && cp "$HOME"/tools/crimson/words/exp/OR "$HOME"/tools/CRIMSON/words/exp/OR && cp "$HOME"/tools/crimson/scripts/crimson_templator.py "$HOME"/tools/CRIMSON/scripts/crimson_templator.py && gem install wpscan && go install github.com/incogbyte/quickpress@latest && git clone --depth 1 https://github.com/linoskoczek/WPluginScanner && cd  WPluginScanner  &&  python3 crawlpopular.py && python3 crawlall.py && cd .. && git clone https://github.com/webarx-security/wpbullet wpbullet  && pip install -r wpbullet/requirements.txt && git clone https://github.com/defparam/smuggler && git clone https://gist.github.com/298d11b3a77b97c908d63a345d3c624d.git hop-by-hop/  &&  cp "$HOME"/tools/crimson/words/exp/hbh-headers "$HOME"/tools/CRIMSON/words/exp/hbh-headers  && apt install -y npm sqlmap  && npm install broken-link-checker -g && git clone https://github.com/ticarpi/jwt_tool  && python3 -m pip install termcolor cprint pycryptodomex requests  && go install github.com/mlcsec/headi@latest && cp "$HOME"/tools/crimson/words/exp/headi.txt "$HOME"/tools/CRIMSON/words/exp/headi.txt  && cp "$HOME"/tools/crimson/scripts/codeql/codeql-js.sh "$HOME"/tools/CRIMSON/scripts/codeql/codeql-js.sh && cp "$HOME"/tools/crimson/scripts/sitemap-urls.sh "$HOME"/tools/CRIMSON/scripts/sitemap-urls.sh && cp /root/tools/crimson/words/BCK_EXT /root/tools/CRIMSON/words/BCK_EXT &&  python3 -m pip install semgrep  && go install github.com/raverrr/plution@latest  && cp "$HOME"/tools/crimson/words/bug "$HOME"/tools/CRIMSON/words/bug && wget https://github.com/github/codeql-cli-binaries/releases/download/v2.6.3/codeql-linux64.zip && unzip codeql-linux64.zip && rm codeql-linux64.zip && rm -rf crimson


### TO DO IN 4TH MODULE:

### STATIC C:
# weggli
sudo apt install cargo -y
sudo cargo install weggli
# cppcheck
sudo apt-get install cppcheck -y
# flawfinder
sudo apt install flawfinder -y 
# graudit
git clone https://github.com/wireghoul/graudit
sudo ln -s graudit/graudit /usr/bin/graudit
# pscan
sudo apt install pscan -y
# cflow 
sudo apt install cflow -y