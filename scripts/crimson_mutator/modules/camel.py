def make_camel(payload):
    camel_payload =""
    for x in range(len(payload)):
        if x%2==0:
            camel_payload+=payload[x].upper()
        else:
            camel_payload+=payload[x].lower()

    return camel_payload

def make_upper(string):
    return string.upper()


def make_lower(string):
    return string.lower()


