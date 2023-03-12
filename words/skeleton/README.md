# HOW TO MERGE IT ==> DIR
1. First copy and name your wordlist as `custom`.
```bash
cp your_wordlist custom
```
2. Then use crimson_wordlister to filter out crap - you can skip this if you don't need it.
```bash
crimson_wordlister.sh
```
3. Merge known and good wordlists with your `custom`
```bash
sort -u 1.dirsearch 2.medium 3.top10000 4.skipfish 5.ws 6.direcotries 7.backups 8.karmaz 9.dirb_big >> skeleton
sort -u skeleton custom > dir
awk '{print length, $0}' dir | sort -n | cut -d " " -f2- > new.txt
cat new.txt | anew custom > dir
rm new.txt
```
