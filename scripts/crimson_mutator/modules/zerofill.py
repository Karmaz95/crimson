# from zerofill import make_zerofill
#Tamper payload, fill it with key words for WAF bypass 

def make_zerofill(string):
    new_string =""
    for x in range(len(string)):
        if string[x] != " ":
            new_string += string[x] + "ZEROFILL"
        else:
            new_string += string[x]
            
    return new_string


