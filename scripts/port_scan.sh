#!/bin/bash
#MAKE DIRS AND FILES 
echo > $HOME/bounty/$DOMAIN/ip.txt
echo > $HOME/bounty/$DOMAIN/ports.txt
#GET IP RANGE && CORESPONDING 
for domain in $(cat $HOME/bounty/$DOMAIN/live.txt);do echo "+++ $domain +++" >> $HOME/bounty/$DOMAIN/ip.txt && dig +short $domain >> $HOME/bounty/$DOMAIN/ip.txt ;done
#SORT && FILTER THE STUFF
cat $HOME/bounty/$DOMAIN/ip.txt | grep -o -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | sort -u > ~/bounty/$DOMAIN/filtered_ip.txt
#GET PORTS
for ip in $(cat $HOME/bounty/$DOMAIN/filtered_ip.txt);do masscan -p1-65535 --max-rate 1000 $ip >> $HOME/bounty/$DOMAIN/ports.txt ; done
rm $HOME/bounty/$DOMAIN/ip.txt
