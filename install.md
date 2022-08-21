# Crimson v3 installer
> Instructions on how to build a docker container with the Crimson latest version by yourself.

1. Start clean Kali distro docker container:
```bash
sudo docker run --network="host" --name crimson -it kalilinux/kali-rolling
```
2. Installator (all YES => 27 => 14 => 1):
```bash
echo "IyMjIFBBVEhTIApleHBvcnQgR09ST09UPS91c3IvbGliL2dvCmV4cG9ydCBHT1BBVEg9JEhPTUUvZ28KZXhwb3J0IFBBVEg9JEdPUEFUSC9iaW46JEdPUk9PVC9iaW46JFBBVEgKZXhwb3J0IENSSU1TT05fUEFUSD0vcm9vdC90b29scy9jcmltc29uCgojIyMgQ1JJTVNPTgphbGlhcyBjcmltc29uPSJjZCAkQ1JJTVNPTl9QQVRIIgphbGlhcyBjXzA9IiRDUklNU09OX1BBVEgvY3JpbXNvbl9JUGNvbiIKYWxpYXMgY18xPSIkQ1JJTVNPTl9QQVRIL2NyaW1zb25fcmVjb24iCmFsaWFzIGNfMj0iJENSSU1TT05fUEFUSC9jcmltc29uX3RhcmdldCIKYWxpYXMgY18zPSIkQ1JJTVNPTl9QQVRIL2NyaW1zb25fZXhwbG9pdCIKCiMjIyBUT09MUwphbGlhcyBiYXQ9ImJhdGNhdCIKYWxpYXMgZmQ9ImZkZmluZCIKYWxpYXMgY21lPSJjcmFja21hcGV4ZWMiCmFsaWFzIHF1aWNrcHJlc3M9Ii9yb290L3Rvb2xzL3F1aWNrcHJlc3MvcXVpY2twcmVzcyIKYWxpYXMgc3NzPSJweXRob24zIC1tIGh0dHAuc2VydmVyIDgwIgphbGlhcyBwc2Jhc2U2NF9lbmNvZGU9Imljb252IC10IHV0Zi0xNmxlIHwgYmFzZTY0IC13IDAiCmFsaWFzIHBhcnNlX25tYXA9InVsdGltYXRlLW5tYXAtcGFyc2VyLnNoICouZ25tYXAgLS1hbGwiCmFsaWFzIGdyZXBfZG9tYWluPSJhd2sgLUYvICd7cHJpbnQgJDN9JyB8IHNvcnQgLXUiCmFsaWFzIGZlcm94PSJmZXJveGJ1c3RlciAtQyA0MDAsNDA0IC0tYXV0by10dW5lICAtbkVnQmVrciAtLXdvcmRsaXN0ICRIT01FL3Rvb2xzL2NyaW1zb24vd29yZHMvZGlyIC1vIGZlcm94LnR4dCAtSSAzZ3AsYWFjLGFwbmcsYXZpZixibXAsY2xhc3MsY29tLGNzcyxjdXIsZG9jLGZsYWMsZ2lmLGd6LGljbyxqYXIsamZpZixqcGVnLGpwZyxtNGEsbTRwLG00dixtb3YsbXAzLG1wNCxtcGVnLG1wZyxvZ2Esb2dnLG9ndixwZGYscGlmLHBqcCxwanBlZyxwbmcscmFtLHNjcixzbnAsc3ZnLHN3Zix0Z3osdGlmLHRpZmYsd2F2LHdlYm0sd2VicCx3b2ZmLHhscyAtdSIKYWxpYXMgY2hlY2tfYmFja3Vwcz0icHl0aG9uICIvcm9vdC90b29scy9jcmltc29uL3NjcmlwdHMvY3JpbXNvbl9iYWNrdXBlci5weSIgLWUgIi9yb290L3Rvb2xzL2NyaW1zb24vd29yZHMvQkNLX0VYVCIgLW8gYmFja3Vwcy50eHQgLXciCgojIyMgRlVOQ1RJT05TCmZ1bmN0aW9uIGdlbl9uZXRfeXNvc2VyaWFsKCkgewogICAgIyBHRU5FUkFURSBZU09TRVJJQUwgUEFZTE9BRFMgVVNJTkcgR0FER0VUUyBGUk9NICRIT01FL3Rvb2xzL2NyaW1zb24vd29yZHMvZXhwL25ldGdhZGdldHMKICAgICMgQVJHWzFdIGlzIHRoZSBjb2xsYWJvcmF0b3IgZG9tYWluCiAgICAjIEVYQU1QTEU6IGdlbl9uZXRfeXNvc2VyaWFsIERPTUFJTi5CUlVQLkNPTQogICAgZm9yIGdhZGdldCBpbiAkKGNhdCAiJEhPTUUvdG9vbHMvY3JpbXNvbi93b3Jkcy9leHAvbmV0Z2FkZ2V0cyIpCiAgICBkbyAKICAgICAgICB3aW5lICIkSE9NRS90b29scy9jcmltc29uL3NjcmlwdHMvR09BU1QvbmV0LXlzb3NlcmlhbC0xMzUveXNvc2VyaWFsLmV4ZSIgLWYgQmluYXJ5Rm9ybWF0dGVyIC1nICIkZ2FkZ2V0IiAtbyBiYXNlNjQgLWMgInBpbmcgJDEiIC9ub2d1aSA+PiBuZXRfZGVzZXJpYWxpemF0aW9uX3BheWxvYWRzLnR4dAogICAgZG9uZQp9CmZ1bmN0aW9uIGdlbl9qYXZhX3lzb3NlcmlhbCgpIHsKICAgICMgR0VORVJBVEUgWVNPU0VSSUFMIFBBWUxPQURTIFVTSU5HIEdBREdFVFMgRlJPTSAkSE9NRS90b29scy9jcmltc29uL3dvcmRzL2V4cC9qYXJnYWRnZXRzCiAgICAjIEFSR1sxXSBpcyB0aGUgY29sbGFib3JhdG9yIGRvbWFpbgogICAgIyBFWEFNUExFOiBnZW5famF2YV95c29zZXJpYWwgRE9NQUlOLkJSVVAuQ09NCiAgICBmb3IgZ2FkZ2V0IGluICQoY2F0ICIkSE9NRS90b29scy9jcmltc29uL3dvcmRzL2V4cC9qYXJnYWRnZXRzIikKICAgIGRvIAogICAgICAgIGphdmEgLWphciAiJEhPTUUvdG9vbHMveXNvc2VyaWFsL3lzb3NlcmlhbC5qYXIiICRnYWRnZXQgIiQxIiB8IGJhc2U2NCAtdzAgPj4gdGVtcF9wYXlsb2Fkcy50eHQgJiYgZWNobyA+PiB0ZW1wX3BheWxvYWRzLnR4dAogICAgZG9uZQogICAgc2VkICcvXiQvZCcgdGVtcF9wYXlsb2Fkcy50eHQgPiBqYXZhX2Rlc2VyaWFsaXphdGlvbl9wYXlsb2Fkcy50eHQKICAgIHJtIHRlbXBfcGF5bG9hZHMudHh0Cn0KCmZ1bmN0aW9uIHJyIHsKICAgICAgICB1bGltaXQgLW4gNTAwMAogICAgICAgIHJ1c3RzY2FuIC1hICIkMSIgLS0gLW4gLUEgLVBuIC0tc2NyaXB0IGRpc2NvdmVyeSx2dWxuIC0tYXBwZW5kLW91dHB1dCAtb0Egc2Nhbgp9CgpmdW5jdGlvbiBzcWxpIHsKICAgICAgICBzcWxtYXAgLWIgLW8gLXYgMCAtLWJhbm5lciAtdSAiJDEiCn0KCmZ1bmN0aW9uIHdvcmRzIHsKICAgICMgSmF2YSBkZXNlcmlhbGl6YXRpb24gcGF5bG9hZCBVUkxETlMgKCogc3dhcCB0aGUgamF2YSBwYXRoIGlmIGRvZXMgbm90IHdvcmspCiAgICBqYXZhIC1qYXIgIiRIT01FIi90b29scy9jcmltc29uL3NjcmlwdHMvR09BU1QveXNvc2VyaWFsLmphciBVUkxETlMgImh0dHA6Ly8kMSIgfCBiYXNlNjQgLXcwIHxzZWQgInMvJC9cbi9nIiA+IG9vYi5mdXp6CiAgICAjIFByZXBhcmluZyBPT0IgcGF5bG9hZGxpc3QgYW5kIGNvcHlpbmcgaXQgdG8gdGhlIGNsaXBib2FyZAogICAgY2F0ICIkSE9NRSIvdG9vbHMvY3JpbXNvbi93b3Jkcy9leHAvT09CIHwgc2VkICJzL2RvbWFpbl9jb2xsYWIvJDEvZyIgfHNlZCAicy92cHNfaXAvJDIvZyIgPj4gb29iLmZ1enoxCiAgICBjYXQgb29iLmZ1enoxIHwgc2VkICJzLyQyOjgwLyQyOiQzL2ciID4+IG9vYi5mdXp6ICYmIHJtIG9vYi5mdXp6MQogICAgY2F0ICIkSE9NRSIvdG9vbHMvY3JpbXNvbi93b3Jkcy9leHAvQkxJTkRfWFNTIHwgc2VkICJzL2RvbWFpbl9jb2xsYWIvJDEvZyIgPj4gb29iLmZ1enoKICAgIGNhdCBvb2IuZnV6eiB8IGNsaXAuZXhlCiAgICAjIFByZXBhcmluZyBvdGhlciB3b3JkbGlzdHMgYW5kIGZpbGVzIHRvIHVwbG9hZAogICAgY2F0ICIkSE9NRSIvdG9vbHMvY3JpbXNvbi93b3Jkcy9idWcgPj4gYnVnLmZ1enoKICAgIGNhdCAiJEhPTUUiL3Rvb2xzL2NyaW1zb24vd29yZHMvZXhwL2h0dHBfbGVha3MgfCBzZWQgInMvZG9tYWluX2NvbGxhYi8kMS9nIiA+PiBodHRwX2xlYWtzCiAgICBjYXQgIiRIT01FIi90b29scy9jcmltc29uL3dvcmRzL2V4cC9ieXBhc3NfZXh0ID4+IGJ5cGFzc19leHQKICAgIGNhdCAiJEhPTUUiL3Rvb2xzL2NyaW1zb24vd29yZHMvZXhwL0JMSU5EX1hTUyB8IHNlZCAicy9kb21haW5fY29sbGFiLyQxL2ciID4+IEJMSU5EX1hTUwogICAgY2F0ICIkSE9NRSIvdG9vbHMvY3JpbXNvbi93b3Jkcy9leHAvaGVhZGVycyB8IHNlZCAicy9kb21haW5fY29sbGFiLyQxL2ciID4+IGhlYWRlcnMuZnV6egogICAgIyBQcmVwYXJpbmcgdXBsb2FkCiAgICBta2RpciB1cGxvYWQKICAgIGNkIHVwbG9hZAogICAgY3AgIiRIT01FIi90b29scy9jcmltc29uL3VwbG9hZC8qIC4KICAgIGNhdCBleGlmdG9vbC5qcGcgfCBzZWQgInMvZG9tYWluX2NvbGxhYi8kMS9nIiA+PiAxMjMgJiYgbXYgMTIzIGV4aWZ0b29sZG9tYWluLmpwZwogICAgY2F0IGV4aWZ0b29sLmpwZyB8IHNlZCAicy9kb21haW5fY29sbGFiLyQyOiQzL2ciID4+IDEyMyAmJiBtdiAxMjMgZXhpZnRvb2x2cHMuanBnCiAgICBjYXQgZm9ybXVsYV9pbmplY3Rpb25zLnR4dCB8IHNlZCAicy9kb21haW5fY29sbGFiLyQxL2ciIHxzZWQgInMvdnBzX2lwLyQyL2ciID4+IGZvcm11bGFfaW5qZWN0aW9uczEKICAgIGNhdCBmb3JtdWxhX2luamVjdGlvbnMxIHwgc2VkICJzLyQyOjgwLyQyOiQzL2ciID4+IGZvcm11bGFfaW5qZWN0aW9ucy50eHQgJiYgcm0gZm9ybXVsYV9pbmplY3Rpb25zMQogICAgY2QgLi4KfQo=" | base64 -d >> $HOME/.bashrc && source $HOME/.bashrc && mkdir -p "$HOME/tools/" && cd "$HOME/tools/" && apt update && apt install -y kali-linux-headless && apt install -y testssl.sh feroxbuster bat fd-find golang brutespray npm jq massdns libcurl4-openssl-dev spiderfoot theharvester node-js-beautify && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install ./google-chrome-stable_current_amd64.deb -y && rm -f google-chrome-stable_current_amd64.deb && curl https://sh.rustup.rs -sSf | sh && source $HOME/.cargo/env && wget https://raw.githubusercontent.com/shifty0g/ultimate-nmap-parser/master/ultimate-nmap-parser.sh -O /usr/bin/ultimate-nmap-parser.sh && chmod +x /usr/bin/ultimate-nmap-parser.sh && pip3 install --upgrade PyCryptodome PyYAML argparse arjun censys certifi chardet colorama cprint fake_useragent future fuzzywuzzy git+https://github.com/rthalley/dnspython.git idna mailspoof py-altdns pyOpenSSL pycryptodomex pycurl  pydig pyvis pywhat requests s3scanner selenium semgrep ssh-audit tabulate termcolor terminaltables tld tqdm urllib3 wfuzz yq && go install github.com/ropnop/kerbrute@latest && go install github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest && go install github.com/raverrr/plution@latest && go install github.com/mlcsec/headi@latest && go install github.com/dwisiswant0/crlfuzz/cmd/crlfuzz@latest && go install github.com/hahwul/dalfox/v2@latest && go install github.com/dwisiswant0/galer@latest && go install github.com/003random/getJS@latest && go install github.com/edoardottt/cariddi@latest && go install github.com/hakluke/hakrawler@latest && go install github.com/jaeles-project/gospider@latest && go install github.com/projectdiscovery/httpx/cmd/httpx@latest && go install github.com/tomnomnom/anew@latest && go install github.com/tomnomnom/qsreplace@latest && go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest && go install github.com/tomnomnom/assetfinder@latest && go install github.com/d3mondev/puredns/v2@latest && go install github.com/faizal3199/dns-wildcard-removal@latest && go install github.com/lc/gau@latest && go install github.com/tomnomnom/waybackurls@latest && go install github.com/sensepost/gowitness@latest && go install github.com/shivangx01b/CorsMe@latest && go install github.com/incogbyte/quickpress@latest && go install github.com/haccer/subjack@latest && go install github.com/tomnomnom/unfurl@latest && go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest && npm install broken-link-checker -g && git clone https://github.com/doyensec/inql.git && git clone https://github.com/vladko312/SSTImap.git && git clone https://github.com/cddmp/enum4linux-ng.git && git clone https://github.com/SpiderLabs/HostHunter.git && git clone --recursive https://github.com/screetsec/Sudomy.git && git clone https://github.com/devanshbatham/ParamSpider && git clone https://github.com/fullhunt/log4j-scan.git && git clone https://gist.github.com/298d11b3a77b97c908d63a345d3c624d.git hop-by-hop/ && git clone https://github.com/Tuhinshubhra/CMSeeK && git clone https://github.com/s0md3v/XSStrike.git && git clone --depth 1 https://github.com/linoskoczek/WPluginScanner && git clone https://github.com/webarx-security/wpbullet wpbullet && git clone https://github.com/defparam/smuggler && git clone https://github.com/ticarpi/jwt_tool && git clone https://github.com/RustScan/RustScan.git && git clone https://github.com/Karmaz95/crimson.git && nuclei -ut -headless && cd RustScan && cargo build --release && cd /usr/local/bin/ && ln -s "$HOME/tools/RustScan/target/release/rustscan" rustscan && cd "$HOME/tools" && cd enum4linux-ng/ && python3 setup.py install && cd .. && python3 "$HOME"/tools/CMSeeK/cmseek.py --update && cd WPluginScanner && python3 crawlpopular.py && python3 crawlall.py && cd .. && cd inql && python3 setup.py install && cd .. && subfinder && clear
```
3. PULLING THE IMAGE
```bash
docker container commit crimson karmaz95/crimson:v3
docker push karmaz95/crimson:v3
```
# CRIMSON .BASHRC ADDITION
```bash
### PATHS 
export GOROOT=/usr/lib/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
export CRIMSON_PATH=/root/tools/crimson

### CRIMSON
alias crimson="cd $CRIMSON_PATH"
alias c_0="$CRIMSON_PATH/crimson_IPcon"
alias c_1="$CRIMSON_PATH/crimson_recon"
alias c_2="$CRIMSON_PATH/crimson_target"
alias c_3="$CRIMSON_PATH/crimson_exploit"

### TOOLS
alias bat="batcat"
alias fd="fdfind"
alias cme="crackmapexec"
alias quickpress="/root/tools/quickpress/quickpress"
alias sss="python3 -m http.server 80"
alias psbase64_encode="iconv -t utf-16le | base64 -w 0"
alias parse_nmap="ultimate-nmap-parser.sh *.gnmap --all"
alias grep_domain="awk -F/ '{print $3}' | sort -u"
alias ferox="feroxbuster -C 400,404 --auto-tune  -nEgBekr --wordlist $HOME/tools/crimson/words/dir -o ferox.txt -I 3gp,aac,apng,avif,bmp,class,com,css,cur,doc,flac,gif,gz,ico,jar,jfif,jpeg,jpg,m4a,m4p,m4v,mov,mp3,mp4,mpeg,mpg,oga,ogg,ogv,pdf,pif,pjp,pjpeg,png,ram,scr,snp,svg,swf,tgz,tif,tiff,wav,webm,webp,woff,xls -u"
alias check_backups="python "/root/tools/crimson/scripts/crimson_backuper.py" -e "/root/tools/crimson/words/BCK_EXT" -o backups.txt -w"

### FUNCTIONS
function gen_net_ysoserial() {
    # GENERATE YSOSERIAL PAYLOADS USING GADGETS FROM $HOME/tools/crimson/words/exp/netgadgets
    # ARG[1] is the collaborator domain
    # EXAMPLE: gen_net_ysoserial DOMAIN.BRUP.COM
    for gadget in $(cat "$HOME/tools/crimson/words/exp/netgadgets")
    do 
        wine "$HOME/tools/crimson/scripts/GOAST/net-ysoserial-135/ysoserial.exe" -f BinaryFormatter -g "$gadget" -o base64 -c "ping $1" /nogui >> net_deserialization_payloads.txt
    done
}
function gen_java_ysoserial() {
    # GENERATE YSOSERIAL PAYLOADS USING GADGETS FROM $HOME/tools/crimson/words/exp/jargadgets
    # ARG[1] is the collaborator domain
    # EXAMPLE: gen_java_ysoserial DOMAIN.BRUP.COM
    for gadget in $(cat "$HOME/tools/crimson/words/exp/jargadgets")
    do 
        java -jar "$HOME/tools/ysoserial/ysoserial.jar" $gadget "$1" | base64 -w0 >> temp_payloads.txt && echo >> temp_payloads.txt
    done
    sed '/^$/d' temp_payloads.txt > java_deserialization_payloads.txt
    rm temp_payloads.txt
}

function rr {
        ulimit -n 5000
        rustscan -a "$1" -- -n -A -Pn --script discovery,vuln --append-output -oA scan
}

function sqli {
        sqlmap -b -o -v 0 --banner -u "$1"
}

function words {
    # Java deserialization payload URLDNS (* swap the java path if does not work)
    java -jar "$HOME"/tools/crimson/scripts/GOAST/ysoserial.jar URLDNS "http://$1" | base64 -w0 |sed "s/$/\n/g" > oob.fuzz
    # Preparing OOB payloadlist and copying it to the clipboard
    cat "$HOME"/tools/crimson/words/exp/OOB | sed "s/domain_collab/$1/g" |sed "s/vps_ip/$2/g" >> oob.fuzz1
    cat oob.fuzz1 | sed "s/$2:80/$2:$3/g" >> oob.fuzz && rm oob.fuzz1
    cat "$HOME"/tools/crimson/words/exp/BLIND_XSS | sed "s/domain_collab/$1/g" >> oob.fuzz
    cat oob.fuzz | clip.exe
    # Preparing other wordlists and files to upload
    cat "$HOME"/tools/crimson/words/bug >> bug.fuzz
    cat "$HOME"/tools/crimson/words/exp/http_leaks | sed "s/domain_collab/$1/g" >> http_leaks
    cat "$HOME"/tools/crimson/words/exp/bypass_ext >> bypass_ext
    cat "$HOME"/tools/crimson/words/exp/BLIND_XSS | sed "s/domain_collab/$1/g" >> BLIND_XSS
    cat "$HOME"/tools/crimson/words/exp/headers | sed "s/domain_collab/$1/g" >> headers.fuzz
    # Preparing upload
    mkdir upload
    cd upload
    cp "$HOME"/tools/crimson/upload/* .
    cat exiftool.jpg | sed "s/domain_collab/$1/g" >> 123 && mv 123 exiftooldomain.jpg
    cat exiftool.jpg | sed "s/domain_collab/$2:$3/g" >> 123 && mv 123 exiftoolvps.jpg
    cat formula_injections.txt | sed "s/domain_collab/$1/g" |sed "s/vps_ip/$2/g" >> formula_injections1
    cat formula_injections1 | sed "s/$2:80/$2:$3/g" >> formula_injections.txt && rm formula_injections1
    cd ..
}
```



# ONE-LINER ATOMS 
> Below you can find what the one-liner actually install:
## KALI HEADLESS - BASE IMAGE
```bash
apt update && apt -y install kali-linux-headless
mkdir -p "$HOME/tools/crimson"
cd "$HOME/tools/"
```
## FDFIND
```bash
apt install fd-find 
```
## GOLANG
```bash
apt install golang
```

## RUST && RUSTSCAN
```bash
curl https://sh.rustup.rs -sSf | sh
source $HOME/.cargo/env
git clone https://github.com/RustScan/RustScan.git && cd RustScan && cargo build --release && cd /usr/local/bin/ && ln -s "$HOME/tools/RustScan/target/release/rustscan" rustscan && cd "$HOME/tools"
```
## ENUM4LINUX
```bash
git clone https://github.com/cddmp/enum4linux-ng.git
cd enum4linux-ng/
python3 setup.py install
cd ..
```

## KERBRUTE
```bash
go install github.com/ropnop/kerbrute@latest
```

## NAMP PARSER
```bash
wget https://raw.githubusercontent.com/shifty0g/ultimate-nmap-parser/master/ultimate-nmap-parser.sh -O /usr/bin/ultimate-nmap-parser.sh
chmod +x /usr/bin/ultimate-nmap-parser.sh
```

## TESTSSL
```bash
apt install -y testssl.sh
```

## NUCLEI + TEMPLATES
```bash
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
nuclei -ut -headless
```

## HTTPX
```bash
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

## DNSX
```bash
go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest
```

## SSH-AUDIT
```bash
pip3 install ssh-audit
```

## FEROXBUSTER
```
apt install -y feroxbuster
```


## MAILSPOOF
```bash
pip3 install mailspoof
```
## HOSTHUNTER
```bash
git clone https://github.com/SpiderLabs/HostHunter.git
python3 -m pip install -r HostHunter/requirements.txt
```

## BRUTESPRAY
```bash
apt install brutespray
```

## ANEW && QSREPLACE
```bash
go install github.com/tomnomnom/anew@latest
go install github.com/tomnomnom/qsreplace@latest
```

## NPM
```bash
apt install npm -y
```

## JQ
```bash
apt install -y jq
```

## UNFURL
```bash
go install github.com/tomnomnom/unfurl@latest
```

## BATCAT
```bash
apt install -y bat
```

## SUBFINDER
```bash
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

## SUDOMY
```bash
git clone --recursive https://github.com/screetsec/Sudomy.git && python3 -m pip install -r Sudomy/requirements.txt
```

## ASSETFINDER
```bash
go install github.com/tomnomnom/assetfinder@latest
```

## PARAMSPIDER
```bash
git clone https://github.com/devanshbatham/ParamSpider && python3 -m pip install -r ParamSpider/requirements.txt
```

## PUREDNS
```bash
go install github.com/d3mondev/puredns/v2@latest
```

## MASSDNS
```bash
apt install -y massdns
```

## DNS-WILDCARD-REMOVAL
```bash
go install github.com/faizal3199/dns-wildcard-removal@latest
```

## ALTDNS
```bash
pip3 install py-altdns==1.0.2
```

## GAU
```bash
GO111MODULE=on go install github.com/lc/gau@latest
```

## WAYBACKURLS
```bash
go install github.com/tomnomnom/waybackurls@latest
```

## GOWITNESS
```bash
go install github.com/sensepost/gowitness@latest
```

## GOOGLE CHROME
```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install ./google-chrome-stable_current_amd64.deb -y
rm -f google-chrome-stable_current_amd64.deb
```

## LATEST DNSPYTHON
> Because dnsrecon error.
```bash
pip install git+https://github.com/rthalley/dnspython.git
```

## CORSME
```bash
go install github.com/shivangx01b/CorsMe@latest
```

## LOG4JSCAN
```bash
git clone https://github.com/fullhunt/log4j-scan.git && pip3 install -r log4j-scan/requirements.txt
```

## GOSPIDER
```bash
GO111MODULE=on go install github.com/jaeles-project/gospider@latest
```

## HAKRAWLER
```bash
go install github.com/hakluke/hakrawler@latest
```

## CARIDDI
```bash
go install github.com/edoardottt/cariddi@latest
```

## GETJS
```bash
go install github.com/003random/getJS@latest
```

## JS-BEAUTIFY
```bash
node-js-beautify
```

## TQDM
```bash
pip install tqdm
```

## SEMGREP
```bash
pip install semgrep
```

## ARJUN
```bash
pip install arjun
```

## HOP-BY-HOP DELETION
```bash
git clone https://gist.github.com/298d11b3a77b97c908d63a345d3c624d.git hop-by-hop/
```

## GALER
```bash
go install github.com/dwisiswant0/galer@latest
```

## CMSEEK
```bash
git clone https://github.com/Tuhinshubhra/CMSeeK
cd CMSeeK
pip install -r requirements.txt
cd ..
python3 "$HOME"/tools/CMSeeK/cmseek.py --update
```

## WFUZZ
```bash
apt install libcurl4-openssl-dev
pip3 install --upgrade pycurl
pip3 install --upgrade wfuzz
```

## XSStrike
```bash
git clone https://github.com/s0md3v/XSStrike.git
cd XSStrike
python3 -m pip install -r requirements.txt
cd ..
```

## DALFOX
```bash
go install github.com/hahwul/dalfox/v2@latest
```

## CRLFUZZ
```bash
GO111MODULE=on go install github.com/dwisiswant0/crlfuzz/cmd/crlfuzz@latest
```

## QUICKPRESS
```bash
go install github.com/incogbyte/quickpress@latest
```

## WPluginScanner
```bash
git clone --depth 1 https://github.com/linoskoczek/WPluginScanner
cd WPluginScanner
python3 crawlpopular.py
python3 crawlall.py
cd ..
```

## WPBULLET
```bash
git clone https://github.com/webarx-security/wpbullet wpbullet
pip install -r wpbullet/requirements.txt
```

## SMUGGLER
```bash
git clone https://github.com/defparam/smuggler
```

## BROKEN LINK CHECKER 
```bash
npm install broken-link-checker -g
```

## JWT_TOOL
```bash
git clone https://github.com/ticarpi/jwt_tool
python3 -m pip install termcolor cprint pycryptodomex requests
```

## HEADI
```bash
go install github.com/mlcsec/headi@latest
```

## PLUTION
```bash
go install github.com/raverrr/plution@latest
```

## SSTIMAP
```bash
git clone https://github.com/vladko312/SSTImap.git
python3 -m pip install -r SSTImap/requirements.txt
```

## INQL
```bash
git clone https://github.com/doyensec/inql.git
python3 setup.py install
```

## S3SCANNER
```bash
pip3 install s3scanner
```

## PYWHAT
```bash
pip3 install pywhat
```

## CIPHEY
```bash
python3 -m pip install ciphey --upgrade
```

## SPIDERFOOT
```bash
apt install spiderfoot
```

## SUBJACK
```
go install github.com/haccer/subjack@latest
```

## THEHARVESTER
```bash
apt install theharvester
```

# KNOWN ISSUES & SOLUTIONS
1. VPN does not work in the container while using WSL2 on Windows.
* Crimson running on WSL in the Docker.
* Want to use VPN.
> You have to run VPN on `Windows`, not on the WSL.


## SUMMARY
### ALL APTS / WGETS / CURLS
```bash
mkdir -p "$HOME/tools/" && cd "$HOME/tools/" && apt update && apt install -y kali-linux-headless && apt install -y testssl.sh feroxbuster bat fd-find golang brutespray npm jq massdns libcurl4-openssl-dev spiderfoot theharvester node-js-beautify && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install ./google-chrome-stable_current_amd64.deb -y && rm -f google-chrome-stable_current_amd64.deb && curl https://sh.rustup.rs -sSf | sh && source $HOME/.cargo/env && wget https://raw.githubusercontent.com/shifty0g/ultimate-nmap-parser/master/ultimate-nmap-parser.sh -O /usr/bin/ultimate-nmap-parser.sh && chmod +x /usr/bin/ultimate-nmap-parser.sh
```

### ALL PIP3
```bash
pip3 install --upgrade PyCryptodome PyYAML argparse arjun censys certifi chardet colorama cprint fake_useragent future fuzzywuzzy git+https://github.com/rthalley/dnspython.git idna mailspoof py-altdns pyOpenSSL pycryptodomex pycurl pydig pyvis pywhat requests s3scanner selenium semgrep ssh-audit tabulate termcolor terminaltables tld tqdm urllib3 wfuzz yq
```

### ALL GO
```bash
go install github.com/ropnop/kerbrute@latest && go install github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest && go install github.com/raverrr/plution@latest && go install github.com/mlcsec/headi@latest && go install github.com/dwisiswant0/crlfuzz/cmd/crlfuzz@latest && go install github.com/hahwul/dalfox/v2@latest && go install github.com/dwisiswant0/galer@latest && go install github.com/003random/getJS@latest && go install github.com/edoardottt/cariddi@latest && go install github.com/hakluke/hakrawler@latest && go install github.com/jaeles-project/gospider@latest && go install github.com/projectdiscovery/httpx/cmd/httpx@latest && go install github.com/tomnomnom/anew@latest && go install github.com/tomnomnom/qsreplace@latest && go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest && go install github.com/tomnomnom/assetfinder@latest && go install github.com/d3mondev/puredns/v2@latest && go install github.com/faizal3199/dns-wildcard-removal@latest && go install github.com/lc/gau@latest && go install github.com/tomnomnom/waybackurls@latest && go install github.com/sensepost/gowitness@latest && go install github.com/shivangx01b/CorsMe@latest && go install github.com/incogbyte/quickpress@latest && go install github.com/haccer/subjack@latest && go install github.com/tomnomnom/unfurl@latest && go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest
```

### ALL NPM
```bash
npm install broken-link-checker -g
```

### ALL GITS
```bash
git clone https://github.com/doyensec/inql.git && git clone https://github.com/vladko312/SSTImap.git && git clone https://github.com/cddmp/enum4linux-ng.git && git clone https://github.com/SpiderLabs/HostHunter.git && git clone --recursive https://github.com/screetsec/Sudomy.git && git clone https://github.com/devanshbatham/ParamSpider && git clone https://github.com/fullhunt/log4j-scan.git && git clone https://gist.github.com/298d11b3a77b97c908d63a345d3c624d.git hop-by-hop/ && git clone https://github.com/Tuhinshubhra/CMSeeK && git clone https://github.com/s0md3v/XSStrike.git && git clone --depth 1 https://github.com/linoskoczek/WPluginScanner && git clone https://github.com/webarx-security/wpbullet wpbullet && git clone https://github.com/defparam/smuggler && git clone https://github.com/ticarpi/jwt_tool && git clone https://github.com/RustScan/RustScan.git && git clone https://github.com/Karmaz95/crimson.git
```

### TOOL INSTALLATIONS & UPDATES
```bash
nuclei -ut -headless && cd RustScan && cargo build --release && cd /usr/local/bin/ && ln -s "$HOME/tools/RustScan/target/release/rustscan" rustscan && cd "$HOME/tools" && cd enum4linux-ng/ && python3 setup.py install && cd .. && python3 "$HOME"/tools/CMSeeK/cmseek.py --update && cd WPluginScanner && python3 crawlpopular.py && python3 crawlall.py && cd .. && cd inql && python3 setup.py install && cd .. && subfinder
```

### ENCODED BASHRC
```bash
echo "IyMjIFBBVEhTIApleHBvcnQgR09ST09UPS91c3IvbGliL2dvCmV4cG9ydCBHT1BBVEg9JEhPTUUvZ28KZXhwb3J0IFBBVEg9JEdPUEFUSC9iaW46JEdPUk9PVC9iaW46JFBBVEgKZXhwb3J0IENSSU1TT05fUEFUSD0vcm9vdC90b29scy9jcmltc29uCgojIyMgQ1JJTVNPTgphbGlhcyBjcmltc29uPSJjZCAkQ1JJTVNPTl9QQVRIIgphbGlhcyBjXzA9IiRDUklNU09OX1BBVEgvY3JpbXNvbl9JUGNvbiIKYWxpYXMgY18xPSIkQ1JJTVNPTl9QQVRIL2NyaW1zb25fcmVjb24iCmFsaWFzIGNfMj0iJENSSU1TT05fUEFUSC9jcmltc29uX3RhcmdldCIKYWxpYXMgY18zPSIkQ1JJTVNPTl9QQVRIL2NyaW1zb25fZXhwbG9pdCIKCiMjIyBUT09MUwphbGlhcyBiYXQ9ImJhdGNhdCIKYWxpYXMgZmQ9ImZkZmluZCIKYWxpYXMgY21lPSJjcmFja21hcGV4ZWMiCmFsaWFzIHF1aWNrcHJlc3M9Ii9yb290L3Rvb2xzL3F1aWNrcHJlc3MvcXVpY2twcmVzcyIKYWxpYXMgc3NzPSJweXRob24zIC1tIGh0dHAuc2VydmVyIDgwIgphbGlhcyBwc2Jhc2U2NF9lbmNvZGU9Imljb252IC10IHV0Zi0xNmxlIHwgYmFzZTY0IC13IDAiCmFsaWFzIHBhcnNlX25tYXA9InVsdGltYXRlLW5tYXAtcGFyc2VyLnNoICouZ25tYXAgLS1hbGwiCmFsaWFzIGdyZXBfZG9tYWluPSJhd2sgLUYvICd7cHJpbnQgJDN9JyB8IHNvcnQgLXUiCmFsaWFzIGZlcm94PSJmZXJveGJ1c3RlciAtQyA0MDAsNDA0IC0tYXV0by10dW5lICAtbkVnQmVrciAtLXdvcmRsaXN0ICRIT01FL3Rvb2xzL2NyaW1zb24vd29yZHMvZGlyIC1vIGZlcm94LnR4dCAtSSAzZ3AsYWFjLGFwbmcsYXZpZixibXAsY2xhc3MsY29tLGNzcyxjdXIsZG9jLGZsYWMsZ2lmLGd6LGljbyxqYXIsamZpZixqcGVnLGpwZyxtNGEsbTRwLG00dixtb3YsbXAzLG1wNCxtcGVnLG1wZyxvZ2Esb2dnLG9ndixwZGYscGlmLHBqcCxwanBlZyxwbmcscmFtLHNjcixzbnAsc3ZnLHN3Zix0Z3osdGlmLHRpZmYsd2F2LHdlYm0sd2VicCx3b2ZmLHhscyAtdSIKYWxpYXMgY2hlY2tfYmFja3Vwcz0icHl0aG9uICIvcm9vdC90b29scy9jcmltc29uL3NjcmlwdHMvY3JpbXNvbl9iYWNrdXBlci5weSIgLWUgIi9yb290L3Rvb2xzL2NyaW1zb24vd29yZHMvQkNLX0VYVCIgLW8gYmFja3Vwcy50eHQgLXciCgojIyMgRlVOQ1RJT05TCmZ1bmN0aW9uIGdlbl9uZXRfeXNvc2VyaWFsKCkgewogICAgIyBHRU5FUkFURSBZU09TRVJJQUwgUEFZTE9BRFMgVVNJTkcgR0FER0VUUyBGUk9NICRIT01FL3Rvb2xzL2NyaW1zb24vd29yZHMvZXhwL25ldGdhZGdldHMKICAgICMgQVJHWzFdIGlzIHRoZSBjb2xsYWJvcmF0b3IgZG9tYWluCiAgICAjIEVYQU1QTEU6IGdlbl9uZXRfeXNvc2VyaWFsIERPTUFJTi5CUlVQLkNPTQogICAgZm9yIGdhZGdldCBpbiAkKGNhdCAiJEhPTUUvdG9vbHMvY3JpbXNvbi93b3Jkcy9leHAvbmV0Z2FkZ2V0cyIpCiAgICBkbyAKICAgICAgICB3aW5lICIkSE9NRS90b29scy9jcmltc29uL3NjcmlwdHMvR09BU1QvbmV0LXlzb3NlcmlhbC0xMzUveXNvc2VyaWFsLmV4ZSIgLWYgQmluYXJ5Rm9ybWF0dGVyIC1nICIkZ2FkZ2V0IiAtbyBiYXNlNjQgLWMgInBpbmcgJDEiIC9ub2d1aSA+PiBuZXRfZGVzZXJpYWxpemF0aW9uX3BheWxvYWRzLnR4dAogICAgZG9uZQp9CmZ1bmN0aW9uIGdlbl9qYXZhX3lzb3NlcmlhbCgpIHsKICAgICMgR0VORVJBVEUgWVNPU0VSSUFMIFBBWUxPQURTIFVTSU5HIEdBREdFVFMgRlJPTSAkSE9NRS90b29scy9jcmltc29uL3dvcmRzL2V4cC9qYXJnYWRnZXRzCiAgICAjIEFSR1sxXSBpcyB0aGUgY29sbGFib3JhdG9yIGRvbWFpbgogICAgIyBFWEFNUExFOiBnZW5famF2YV95c29zZXJpYWwgRE9NQUlOLkJSVVAuQ09NCiAgICBmb3IgZ2FkZ2V0IGluICQoY2F0ICIkSE9NRS90b29scy9jcmltc29uL3dvcmRzL2V4cC9qYXJnYWRnZXRzIikKICAgIGRvIAogICAgICAgIGphdmEgLWphciAiJEhPTUUvdG9vbHMveXNvc2VyaWFsL3lzb3NlcmlhbC5qYXIiICRnYWRnZXQgIiQxIiB8IGJhc2U2NCAtdzAgPj4gdGVtcF9wYXlsb2Fkcy50eHQgJiYgZWNobyA+PiB0ZW1wX3BheWxvYWRzLnR4dAogICAgZG9uZQogICAgc2VkICcvXiQvZCcgdGVtcF9wYXlsb2Fkcy50eHQgPiBqYXZhX2Rlc2VyaWFsaXphdGlvbl9wYXlsb2Fkcy50eHQKICAgIHJtIHRlbXBfcGF5bG9hZHMudHh0Cn0KCmZ1bmN0aW9uIHJyIHsKICAgICAgICB1bGltaXQgLW4gNTAwMAogICAgICAgIHJ1c3RzY2FuIC1hICIkMSIgLS0gLW4gLUEgLVBuIC0tc2NyaXB0IGRpc2NvdmVyeSx2dWxuIC0tYXBwZW5kLW91dHB1dCAtb0Egc2Nhbgp9CgpmdW5jdGlvbiBzcWxpIHsKICAgICAgICBzcWxtYXAgLWIgLW8gLXYgMCAtLWJhbm5lciAtdSAiJDEiCn0KCmZ1bmN0aW9uIHdvcmRzIHsKICAgICMgSmF2YSBkZXNlcmlhbGl6YXRpb24gcGF5bG9hZCBVUkxETlMgKCogc3dhcCB0aGUgamF2YSBwYXRoIGlmIGRvZXMgbm90IHdvcmspCiAgICBqYXZhIC1qYXIgIiRIT01FIi90b29scy9jcmltc29uL3NjcmlwdHMvR09BU1QveXNvc2VyaWFsLmphciBVUkxETlMgImh0dHA6Ly8kMSIgfCBiYXNlNjQgLXcwIHxzZWQgInMvJC9cbi9nIiA+IG9vYi5mdXp6CiAgICAjIFByZXBhcmluZyBPT0IgcGF5bG9hZGxpc3QgYW5kIGNvcHlpbmcgaXQgdG8gdGhlIGNsaXBib2FyZAogICAgY2F0ICIkSE9NRSIvdG9vbHMvY3JpbXNvbi93b3Jkcy9leHAvT09CIHwgc2VkICJzL2RvbWFpbl9jb2xsYWIvJDEvZyIgfHNlZCAicy92cHNfaXAvJDIvZyIgPj4gb29iLmZ1enoxCiAgICBjYXQgb29iLmZ1enoxIHwgc2VkICJzLyQyOjgwLyQyOiQzL2ciID4+IG9vYi5mdXp6ICYmIHJtIG9vYi5mdXp6MQogICAgY2F0ICIkSE9NRSIvdG9vbHMvY3JpbXNvbi93b3Jkcy9leHAvQkxJTkRfWFNTIHwgc2VkICJzL2RvbWFpbl9jb2xsYWIvJDEvZyIgPj4gb29iLmZ1enoKICAgIGNhdCBvb2IuZnV6eiB8IGNsaXAuZXhlCiAgICAjIFByZXBhcmluZyBvdGhlciB3b3JkbGlzdHMgYW5kIGZpbGVzIHRvIHVwbG9hZAogICAgY2F0ICIkSE9NRSIvdG9vbHMvY3JpbXNvbi93b3Jkcy9idWcgPj4gYnVnLmZ1enoKICAgIGNhdCAiJEhPTUUiL3Rvb2xzL2NyaW1zb24vd29yZHMvZXhwL2h0dHBfbGVha3MgfCBzZWQgInMvZG9tYWluX2NvbGxhYi8kMS9nIiA+PiBodHRwX2xlYWtzCiAgICBjYXQgIiRIT01FIi90b29scy9jcmltc29uL3dvcmRzL2V4cC9ieXBhc3NfZXh0ID4+IGJ5cGFzc19leHQKICAgIGNhdCAiJEhPTUUiL3Rvb2xzL2NyaW1zb24vd29yZHMvZXhwL0JMSU5EX1hTUyB8IHNlZCAicy9kb21haW5fY29sbGFiLyQxL2ciID4+IEJMSU5EX1hTUwogICAgY2F0ICIkSE9NRSIvdG9vbHMvY3JpbXNvbi93b3Jkcy9leHAvaGVhZGVycyB8IHNlZCAicy9kb21haW5fY29sbGFiLyQxL2ciID4+IGhlYWRlcnMuZnV6egogICAgIyBQcmVwYXJpbmcgdXBsb2FkCiAgICBta2RpciB1cGxvYWQKICAgIGNkIHVwbG9hZAogICAgY3AgIiRIT01FIi90b29scy9jcmltc29uL3VwbG9hZC8qIC4KICAgIGNhdCBleGlmdG9vbC5qcGcgfCBzZWQgInMvZG9tYWluX2NvbGxhYi8kMS9nIiA+PiAxMjMgJiYgbXYgMTIzIGV4aWZ0b29sZG9tYWluLmpwZwogICAgY2F0IGV4aWZ0b29sLmpwZyB8IHNlZCAicy9kb21haW5fY29sbGFiLyQyOiQzL2ciID4+IDEyMyAmJiBtdiAxMjMgZXhpZnRvb2x2cHMuanBnCiAgICBjYXQgZm9ybXVsYV9pbmplY3Rpb25zLnR4dCB8IHNlZCAicy9kb21haW5fY29sbGFiLyQxL2ciIHxzZWQgInMvdnBzX2lwLyQyL2ciID4+IGZvcm11bGFfaW5qZWN0aW9uczEKICAgIGNhdCBmb3JtdWxhX2luamVjdGlvbnMxIHwgc2VkICJzLyQyOjgwLyQyOiQzL2ciID4+IGZvcm11bGFfaW5qZWN0aW9ucy50eHQgJiYgcm0gZm9ybXVsYV9pbmplY3Rpb25zMQogICAgY2QgLi4KfQo=" | base64 -d >> $HOME/.bashrc && source $HOME/.bashrc
```