#
### CREATED BY KARMAZ
#
### FUNCTIONS:
#
# 1. CLEAN WORDLISTS WITH VARIOUS FILTERS LISTED BELOW
#
###

### CLEAR TRASH WORDS
sort -u custom | grep -i -v "chuj\|kurwa\|szmata\|pizda\|dziwka\|gay\|lesbi\|porn\|fuck\|shit\|sex\|asshole\|bastard\|bitch\|bollock\|christ\|jesus\|cock\|nigga\|prick\|piss\|slut\|whore\|fetish\|bdsm\|dildo\|penis\|anus\|fellatio\|blowjob\|suck\|booty\|castration\|orgasm\|orgazm\|dick\|ciota\|condom\|kondom\|elakulat\|ejaculation\|sperma\|sperm\|jizz\|seemen\|erotic\|eroty\|erekcja\|erection\|eunuch\|eunich\|facesi\|facial\|spust\|philia\|hustler\|prostitute\|prostytu\|jerk\|kinky\|latex\|libido\|lube\|lubricant\|lubrykant\|sochism\|mastur\|onani\|orgy\|orgia\|penet\|rimmin\|transves\|viagra\|vibrat\|wibrat\|wiagra\|venerea\|vasectomy\|wazektomia\|xxx\|xvideo" | > temp123
mv temp123 custom

### CLEAR DIRECTORY DEPTH +2 ( asd/asd/ )
sort -u custom | grep -v -E "^.*\/.*\/" > temp123
mv temp123 custom

### CLEAR  CHINESE / ARABIC / CYRYLIC / GREEK / THAI
sort -u custom | grep -v -P '[\p{Han}]' | grep -v -P '[\p{Arabic}]' | grep -v -P '[\p{Cyrillic}]' | grep -v -P '[\p{Greek}]' | grep -v -P '[\p{Thai}]'  > temp123
mv temp123 custom

### CLEAR TRIPLE CHAR IN A ROW LINES (without www)
sort -u custom | grep -v -i "aaa\|bbb\|ccc\|ddd\|eee\|fff\|ggg\|hhh\|iii\|jjj\|kkk\|lll\|mmm\|nnn\|ooo\|ppp\|qqq\|rrr\|sss\|ttt\|uuu\|vvv\|www\|xxx\|yyy\|zzz" > temp123
mv temp123 custom

### DETELE FIRST SLASH ( / )
sort -u custom | sed "/^\//d" > temp123
mv temp123 custom

### DELETE LAST SLASH (asd/)
sort -u custom | sed "s/\/$//" > temp123
sort -u temp123 > custom

### DELETE LINES STARTING WITH 4 DIGITS
sort -u custom | sed "/^[0-9][0-9][0-9][0-9].*/d" > temp123

### DELETE LINES WITH ,
sort -u custom | grep -v "^[a-Z].*," | grep -v "^[0-9].*," > temp123
mv temp123 custom

### DELETE LINES WITH MORE THAN 35 CHARS
sort -u custom | grep -v "..................................." > temp123
mv temp123 custom

### DELETE “BACKUP” LINES
sort -u custom | grep -v "^~" > temp123
mv temp123 custom

### DELETE LINES WITH SPACES
sort -u custom | sed "/\ /d" > temp123
mv temp123 custom

### DELETE LINES WITH QUESTION MARK “?” ( except first “?" )
#sort -u custom | grep -v "^?$" | grep -v "?" > temp123
#mv temp123 custom

### CLEAN DOTS ( ..+)
sort -u custom | grep -v "^.*\.[a-Z].*\." | grep -v "^.*\.[0-9].*\." | grep -v "\.\.\.[^\.\/]" | grep -v "[a-Z]\.\." | grep -v "\.\.[a-Z]" | grep -v "\.\." > temp123
mv temp123 custom

### DELETE LINES WITH THREE NUMBERS IN A ROW
sort -u custom | grep -v "[0-9][0-9][0-9]" > temp123
mv temp123 custom

### DELETE ALL LINES WITH 3 “_” IN A STRING
sort -u custom | grep -v "^.*_.*_.*_" > temp123
mv temp123 custom

### SORT BY LENGTH
awk '{print length, $0}' custom | sort -n | cut -d " " -f2- > new.txt
mv new.txt custom

### ANOTHER GARBAGE CLEANER (HARD)
#cat custom | awk '{gsub(/[[:punct:]]/,"")}1' | tr A-Z a-z | sed 's/[0-9]*//g' | sed -e 's/ //g' | strings | tr -cs '[:alpha:]' '\ ' | sed -e 's/ /\n/g' | tr A-Z a-z | sort -u > clean_custom
