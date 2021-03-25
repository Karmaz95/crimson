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
* Create a "manual_payloads.txt" wordlist with payloads to use and place it in the same directory.
* Start the ./crimson_opener.py  -u -l -o
* Open single URL                -u https://url/FUZZ 
* Open wordlist(with fuzzing)    -l [lists_with_urls/FUZZ] 
* Open wordlist(without fuzzing) -o [list_with_urls]
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
0. Create 4 wordlists as described above
1. Start the script: python crimson_payloader

