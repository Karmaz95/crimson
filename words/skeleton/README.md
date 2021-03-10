# HOW TO MERGE IT ==> DIR
cp your_wordlist custom 
crimson_wordlister.sh
	
sort -u 1.dirsearch 2.medium 3.top10000 4.skipfish 5.ws 6.direcotries 7.backups 8.bug >> skeleton
sort -u skeleton custom > dir
awk '{print length, $0}' dir | sort -n | cut -d " " -f2- > new.txt
mv new.txt dir
