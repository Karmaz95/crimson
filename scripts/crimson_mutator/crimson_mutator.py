#!/usr/bin/python
# coding: utf-8
#
### CREATED BY KARMAZ
#
#
#### FUNCTIONS:
#   
#   0.  Mutate your wordlist with below techniques
#   1.  CaMeL CaSe
#   2.  Full URL encoding
#   3.  Double URL encoding
#   4.  Triple URL encoding
#   5.  ZEROFILL keyword between each letter
#   6.  Spaces changed for [+] sign
#   7.  Spaces changed for [+] sign and encode rest as url
#   8.  URL key chars encoded
#   9.  Upcase
#   10. Downcase
#
### LISTS:
#
#   1. mutatations.txt
#
###

from camel import make_camel, make_upper, make_lower
from zerofill import make_zerofill
from url_encoding import make_url, make_plus, make_plus_encoded, make_key_url
import sys
import os

def option_1():
    '''Camel - every even letter in payload is changed to uppercase'''
    mutation_1 = ""
    with open(sys.argv[1]) as payloads:
        for payload in payloads:
            mutation_1+=make_camel(payload)
        
        print mutation_1
        f = open("mutation_1.txt", "w")
        f.write(mutation_1)
        f.close()


def option_2():
    '''Full  URL encoding '''
    mutation_2 = ""
    with open(sys.argv[1]) as payloads:
        for payload in payloads:
            mutation_2 += make_url(payload) + "\n"
        
        print mutation_2.rstrip()
        f = open("mutation_2.txt", "w")
        f.write(mutation_2)
        f.close()


def option_3():
    '''Double URL encoding'''
    mutation_3 = ""
    with open(sys.argv[1]) as payloads:
        for payload in payloads:
            mutation_3 += make_url(make_url(payload)) + "\n"
        
        print mutation_3.rstrip()
        f = open("mutation_3.txt", "w")
        f.write(mutation_3)
        f.close()


def option_4():
    '''Triple URL encoding'''
    mutation_4 = ""
    with open(sys.argv[1]) as payloads:
        for payload in payloads:
            mutation_4 += make_url(make_url(make_url(payload))) + "\n"
        
        print mutation_4.rstrip()
        f = open("mutation_4.txt", "w")
        f.write(mutation_4)
        f.close()



def option_5():
    '''ZEROFILL - add keywords into a payloads'''
    mutation_5 = ""
    with open(sys.argv[1]) as payloads:
        for payload in payloads:
            mutation_5 += make_zerofill(payload)
        
        print mutation_5.rstrip()
        f = open("mutation_5.txt", "w")
        f.write(mutation_5)
        f.close()

   

def option_6():
    '''Change space for plus sign'''
    mutation_6 = ""
    with open(sys.argv[1]) as payloads:
        for payload in payloads:
            mutation_6 += make_plus(payload)
        
        print mutation_6.rstrip()
        f = open("mutation_6.txt", "w")
        f.write(mutation_6)
        f.close()


def option_7():
    '''Change space for plus sign and encode rest'''
    mutation_7 = ""
    with open(sys.argv[1]) as payloads:
        for payload in payloads:
            mutation_7 += make_plus_encoded(payload.rstrip()) + "\n"
        
        print mutation_7.rstrip()
        f = open("mutation_7.txt", "w")
        f.write(mutation_7)
        f.close()



def option_8():
    '''Encode key chars as URL'''
    mutation_8 = ""
    with open(sys.argv[1]) as payloads:
        for payload in payloads:
            mutation_8 += make_key_url(payload.rstrip()) + "\n"
        
        print mutation_8.rstrip()
        f = open("mutation_8.txt", "w")
        f.write(mutation_8)
        f.close()



def option_9():
    '''Make uocase letters'''
    mutation_9 = ""
    with open(sys.argv[1]) as payloads:
        for payload in payloads:
            mutation_9 += make_upper(payload)
        
        print mutation_9.rstrip()
        f = open("mutation_9.txt", "w")
        f.write(mutation_9)
        f.close()



def option_10():
    '''Make downcase letter'''
    mutation_10 = ""
    with open(sys.argv[1]) as payloads:
        for payload in payloads:
            mutation_10 += make_lower(payload)
        
        print mutation_10.rstrip()
        f = open("mutation_10.txt", "w")
        f.write(mutation_10)
        f.close()

           
    
def option_11():
    '''Do all mutations and save it as "mutations.txt"'''
    option_1()
    option_2()
    option_3()
    option_4()
    option_5()
    option_6()
    option_7()
    option_8()
    option_9()
    option_10()
    os.system("cat mutation_* > mutations.txt && rm mutation_* ")


def main():
    print("""\033[0;31m

 ██████╗██████╗ ██╗███╗   ███╗███████╗ ██████╗ ███╗   ██╗        ███╗   ███╗██╗   ██╗████████╗ █████╗ ████████╗ ██████╗ ██████╗
██╔════╝██╔══██╗██║████╗ ████║██╔════╝██╔═══██╗████╗  ██║        ████╗ ████║██║   ██║╚══██╔══╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║     ██████╔╝██║██╔████╔██║███████╗██║   ██║██╔██╗ ██║        ██╔████╔██║██║   ██║   ██║   ███████║   ██║   ██║   ██║██████╔╝
██║     ██╔══██╗██║██║╚██╔╝██║╚════██║██║   ██║██║╚██╗██║        ██║╚██╔╝██║██║   ██║   ██║   ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║██║██║ ╚═╝ ██║███████║╚██████╔╝██║ ╚████║███████╗██║ ╚═╝ ██║╚██████╔╝   ██║   ██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝\033[0m""")
    print("\n\tUSAGE: python crimson_mutator [list_with_payloads]\n")
    print("TECHNIQUES:")
    print("[1]  CaMeL CaSe")
    print("[2]  Full URL encoding")
    print("[3]  Double URL encoding")
    print("[4]  Triple URL encoding")
    print("[5]  ZEROFILL keyword between each letter")
    print("[6]  Spaces changed for [+] sign")
    print("[7]  Spaces changed for [+] sign and encode rest as url")
    print("[8]  URL key chars encoded")
    print("[9]  Upcase")
    print("[10] Downcase")
    print("[11] All mutations")
    print("\n")

    option = raw_input("Chose technique: ")

    if option == "1":
        option_1()
    elif option == "2":
        option_2()
    elif option == "3":
        option_3()
    elif option == "4":
        option_4()
    elif option == "5":
        option_5()
    elif option == "6":
        option_6()
    elif option == "7":
        option_7()
    elif option == "8":
        option_8()
    elif option == "9":
        option_9()
    elif option == "10":
        option_10()
    elif option == "11":
        option_11()
    else:
        exit()

main()
