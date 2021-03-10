# coding: utf-8
#
### CREATED BY KARMAZ
#
#
### FUNCTIONS:
#   
# 1.Combine 4 wordlists into one "payloads.txt".
#
# Wordlists:
#   1) affix    (breaker)   - this wordlist contains char or chars that break the syntax f.e. ' (single quote)
#   2) main     (payload)   - this wordlist contains core of your payload f.e. or 1=1
#   3) suffix   (comment)   - this wordlist contains char or chars that are at the end of payload f.e. # (hash sign)
#   4) add      (addons)    - this wordlist contains working payloads, it will be added at the end of payloads.txt
#
### WORKFLOW
# 0. Create 4 wordlists as described above
# 1. Start the script: python crimson_payloader
###

def load_affix(affix):
    '''Load breakers into an array'''
    affix_wordlist = ""
    with open(affix) as affixes:
        for affix in affixes:
            affix_wordlist += affix

    return(affix_wordlist.split("\n"))


def load_main(main):
    '''Load core of payload into an array'''
    main_wordlist = ""
    with open(main) as mains:
        for main in mains:
            main_wordlist += main

    return(main_wordlist.split("\n"))


def load_suffix(suffix):
    '''Load comments into an array'''
    suffix_wordlist = ""
    with open(suffix) as suffixes:
        for suffix in suffixes:
            suffix_wordlist += suffix
    
    return(suffix_wordlist.split("\n"))


def load_add(add):
    '''Load addons into an array'''
    add_wordlist = ""
    with open(add) as adds:
        for add in adds:
            add_wordlist += add

    return(add_wordlist.split("\n"))


def main():
    '''Load wordlists into an variable and combine them into "payloads.txt"'''
    print("""
    payloads = ""
    affix_list = load_affix("affix")
    main_list = load_main("main")
    suffix_list = load_suffix("suffix")
    add_list = load_add("add")
    for affix in affix_list[:-1]: # without last element which is blank [:-1]
        for main in main_list[:-1]:
            for suffix in suffix_list[:-1]:
                payloads += affix + main + suffix + "\n" 

    for add in add_list[:-1]:
        payloads += add + "\n"

    print(payloads)
    f = open("payloads.txt", "w")
    f.write(payloads)
    f.close


main()
