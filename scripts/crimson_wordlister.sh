### DETELE FIRST SLASH ( / )
sort -u custom | sed "s/^\///" > temp123
mv temp123 custom

### DELETE LAST SLASH (asd/)
sort -u custom | sed "s/\/$//" > temp123
mv temp123 custom

### DELETE FIRST *
sort -u custom | sed "s/^\*//" > temp123
mv temp123 custom

### DELETE LAST *
sort -u custom | sed "s/\*$//" > temp123
mv temp123 custom

### DELETE FIRST ?
sort -u custom | sed "s/^\?//" > temp123
mv temp123 custom

### DELETE LAST ?
sort -u custom | sed "s/\?$//" > temp123
mv temp123 custom

### DELETE FIRST :
sort -u custom | sed "s/^\://" > temp123
mv temp123 custom

### DELETE LAST :
sort -u custom | sed "s/\:$//" > temp123
mv temp123 custom

### DELETE ALL FIRST SPACES
sort -u custom | sed "s/^\ *//" > temp123
mv temp123 custom

### DELETE LAST SPACE
sort -u custom | sed "s/\ *$//" > temp123
mv temp123 custom

### DELETE COMMENTS LINES
sort -u custom | sed "/^\#/d" > temp123
mv temp123 custom

### DELETE LINES STARTED FROM &
sort -u custom | sed "/^\&/d" > temp123
mv temp123 custom

### REMOVE NON ASCII CHARS
sed -i '/[^\x00-\x7F]/d' custom

### USE THE ABOVE COMMANDS MULTIPLE TIMES TO REMOVE RECURSIVE /*/*/ /?/?/ ETC. ### 


### CLEAR  CHINESE / ARABIC / CYRYLIC / GREEK / THAI
sort -u custom | grep -v -P '[\p{Han}]' | grep -v -P '[\p{Arabic}]' | grep -v -P '[\p{Cyrillic}]' | grep -v -P '[\p{Greek}]' | grep -v -P '[\p{Thai}]'  > temp123
mv temp123 custom

### CLEAR TRIPLE CHAR IN A ROW LINES (without www)
sort -u custom | grep -v -i "aaa\|bbb\|ccc\|ddd\|eee\|fff\|ggg\|hhh\|iii\|jjj\|kkk\|lll\|mmm\|nnn\|ooo\|ppp\|qqq\|rrr\|sss\|ttt\|uuu\|vvv\|www\|xxx\|yyy\|zzz" > temp123
mv temp123 custom

### CLEAR TRASH WORDS
sort -u custom | grep -i -v "chuj\|kurwa\|szmata\|pizda\|dziwka\|gay\|lesbi\|porn\|fuck\|shit\|sex\|asshole\|bastard\|bitch\|bollock\|christ\|jesus\|cock\|nigga\|prick\|piss\|slut\|whore\|fetish\|bdsm\|dildo\|penis\|anus\|fellatio\|blowjob\|suck\|booty\|castration\|orgasm\|orgazm\|dick\|ciota\|condom\|kondom\|elakulat\|ejaculation\|sperma\|sperm\|jizz\|seemen\|erotic\|eroty\|erekcja\|erection\|eunuch\|eunich\|facesi\|facial\|spust\|philia\|hustler\|prostitute\|prostytu\|jerk\|kinky\|latex\|libido\|lube\|lubricant\|lubrykant\|sochism\|mastur\|onani\|orgy\|orgia\|penet\|rimmin\|transves\|viagra\|vibrat\|wibrat\|wiagra\|venerea\|vasectomy\|wazektomia\|xxx\|xvideo" > temp123
mv temp123 custom

### DELETE LINES STARTING WITH 4 DIGITS
sed "/^[0-9][0-9][0-9][0-9].*/d" -i custom

### DELETE LINES WITH ,
sort -u custom | grep -v ',' > temp123
mv temp123 custom

### DELETE LINES WITH MORE THAN 35 CHARS
sort -u custom | grep -vE '^.{36,}$' > temp123
mv temp123 custom

### DELETE “BACKUP” LINES
#sort -u custom | grep -v "^~" > temp123
#mv temp123 custom

### DELETE LINES WITH SPACES
sort -u custom | sed "/\ /d" > temp123
mv temp123 custom

### CLEAN DOTS ( ..+)
sort -u custom | grep -vE '\.{2,}' > temp123
mv temp123 custom

### DELETE LINES WITH THREE NUMBERS IN A ROW
#sort -u custom | grep -v "[0-9][0-9][0-9]" > temp123
#mv temp123 custom

### DELETE ALL LINES WITH 3 “_” IN A STRING
sort -u custom | grep -v "^.*_.*_.*_" > temp123
mv temp123 custom

### CLEAR DIRECTORY DEPTH +2 ( asd/asd/ )
sort -u custom | grep -v -E "^.*\/.*\/" > temp123
mv temp123 custom

### SORT BY LENGTH
awk '{print length, $0}' custom | sort -n | cut -d " " -f2- > temp123
mv temp123 custom
