### Endpoints scrapping + burp proxing from a file
export cookie="Cookie: a=1;";
for domain in $(cat $1); do
    echo $domain;
    export domain="$domain";
    ### SPIDER 1 > urls.txt
    echo "\033[0;31m [+]\033[0m STARTING SPIDERS"
    echo "\033[0;31m [+]\033[0m SPIDER [1]"
    echo $domain | httpx -silent | gospider -c 10 -q -r -w -a --sitemap --robots --subs -H $cookie >> urls.txt

    ### SPIDER 2 >> urls.txt
    echo "\033[0;31m [+]\033[0m SPIDER [2]"
    python3 $HOME/tools/ParamSpider/paramspider.py -d $domain --output ./paramspider.txt --level high > /dev/null 2>&1
    cat paramspider.txt | grep http | sort -u | grep $domain >> urls.txt
    rm paramspider.txt

    ### SPIDER 3 >> urls.txt
    echo "\033[0;31m [+]\033[0m SPIDER [3]"
    get-all-urls $domain >> urls.txt

    ### SPIDER 4 >> urls.txt
    echo "\033[0;31m [+]\033[0m SPIDER [4]"
    waybackurls $domain >> urls.txt

    ### SPIDER 5 >> urls.txt
    echo "\033[0;31m [+]\033[0m SPIDER [5]"
    echo $domain | httpx -silent | hakrawler >> urls.txt

    ### SPIDER 6 >> urls.txt
    echo "\033[0;31m [+]\033[0m SPIDER [6]"
    echo $domain | httpx -silent | galer -s >> urls.txt
done

### MERGE SPIDERS AND DELETE DUPLICATES >> urls.txt
echo "\033[0;31m [+]\033[0m MERGING SPIDERS RESULTS"
cat urls.txt | qsreplace -a > temp1.txt
mv temp1.txt urls.txt
### PROXY ALL URLS TO BRUP
wfuzz -L -Z -z file,urls.txt -z file,$HOME/tools/CRIMSON/words/blank -p 127.0.0.1:8080 FUZZFUZ2Z
