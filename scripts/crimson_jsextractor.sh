#!/bin/bash
#
### CREATED BY KARMAZ 
#
#
###TO DO: 
# 1. ADD LINKFINDER
### FUNCTIONS
# 1. GET ENDPOINTS FROM URLS
### 
# USAGE EXAMPLE:
#	extract [url]
#	extract -l wordlist.txt	
###
# !!! REMEMBER to check urls_zile.txt for AUTH KEYS! - Take a look manualy and with crimson_secrets.
#
##
while getopts "u:l:" OPTION; do
    case $OPTION in
    u)
        one_url=$OPTARG
        ;;
    l)
        list_of_url=$OPTARG
        ;;
    *)
        echo "Incorrect options provided"
        exit 1
        ;;
    esac
done


if [ -z $list_of_url ]; 
then
        for line in $(cat $list_of_url); do echo Download the source code of: $line && curl -s $line >> source_of_js.txt; done
        cat source_of_js.txt | ~/tools/relative-url-extractor/extract.rb >> urls_extractor.txt
        cat source_of_js.txt | python3 ~/tools/zile/zile.py >> urls_zile.txt
        cat urls_zile.txt | cut -d " " -f 2 | sed "s/^..//g" | sed "s/..$//g" | sed "s/\"//g" >> extracted_urls.txt
        cat urls_extractor.txt | sed '/^\/$/d' | sed 's/\/\//\//' >> extracted_urls.txt
elif [ -z $one_url ];
then
        echo Download the source code of $one_url && curl -s $one_url >> source_of_js.txt
        cat source_of_js.txt | ~/tools/relative-url-extractor/extract.rb >> urls_extractor.txt
        cat source_of_js.txt | python3 ~/tools/zile/zile.py >> urls_zile.txt
        cat urls_zile.txt  | cut -d " " -f 2 | sed "s/^..//g" | sed "s/..$//g" | sed "s/\"//g" | sed "s/'//g" |sort -u >> extracted_urls.txt
        cat urls_extractor.txt | grep -v "^ " | sed '/^\/$/d' | sed 's/\/\//\//' |sort -u >> extracted_urls.txt
else
        echo -----------
        echo DESCRIPTION:
        echo "  This script gather source code of the single URL or list of URLs and then search for endpoints and auth keys."
        echo ----------
        echo "USAGE: "
        echo "  extract.sh -l wordlist.txt       - extract source code and endpoints from list of urls "
        echo "  extract.sh -u url                - extract source code and endpoints from url "
fi
