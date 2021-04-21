####
# Prerequisites:
# unfurl		-> go get -u github.com/tomnomnom/unfurl			-> https://github.com/tomnomnom/unfurl
# getJS			-> go get github.com/003random/getJS				-> https://github.com/003random/getJS
# codeQL CLI 	-> https://github.com/github/codeql-cli-binaries
# js-beautify	-> pip install jsbeautifier							-> https://github.com/beautify-web/js-beautify

# Usage:
# ./codeql-js.sh https://site number_of_threads burp
# e.g 1 -> download js files by GetJS
# ./codeql-js.sh https://example.com 5
# or use existing js files in this directory
# ./codeql-js.sh https://example.com 5 burp

# Default:
# -j 5 # threads

# Results
# $ cat *.csv

# Errors -> happens, just re-run. If files have not been changed codeql queries will not rerun

# Manual for the findings: 
# https://codeql.github.com/codeql-query-help/javascript/

# Example output from the results file:
# "Client-side cross-site scripting","Writing user input directly to the DOM allows for a cross-site scripting vulnerability.","error","Cross-site scripting vulnerability due to [[""user-provided value""|""relative:///xxx-es5.123.js:40415:30:40415:44""]].","/main-es5.123.js","1337","12","1337","12"
####

if echo "$2" | grep -qE '^[0-9]+$'; then
	echo "Valid number of threads: $2"
else
	echo "Error: invalid number of threads"
	exit -1
fi

host=`echo $1 | unfurl domain`
echo "Domain name: $host"

if [[ "$3" != burp ]]
then
	echo "Downloading JS"
	getJS --url $1 --complete | xargs wget -N
else 
	echo 'Using existing js files in this directory'
    find . -maxdepth 1 -name "*\.js*" -type f
	#find . -type f -maxdepth 1 -name "*.js"
fi

echo "Beautify JS"
find . -type f -maxdepth 1 -name "*.js" -exec js-beautify -r {} \; 

echo "Create database"
codeql database create $host --language=javascript 

echo "Git cloning vscode-codeql-starter workspace"
git clone --recursive https://github.com/github/vscode-codeql-starter.git

echo "CodeQL Database analyzing"
# Base
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-020 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-022 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-078 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-079 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-089 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-094 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-116 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-117 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-134 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-200 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-201 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-209 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-295 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-312 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-313 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-327 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-338 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-346 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-352 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-400 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-451 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-502 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-506 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-601 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-611 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-640 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-643 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-730 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-754 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-770 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-776 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-798 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-807 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-829 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-834 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-843 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-912 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-915 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-916 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/Security/CWE-918 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2

# Experimental
#codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/experimental/Security/CWE-020 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/experimental/Security/CWE-090 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/experimental/Security/CWE-347 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/experimental/Security/CWE-614 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
#codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/experimental/Security/CWE-770 --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2

# Additional
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/AngularJS --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/DOM --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
codeql database analyze $host vscode-codeql-starter/ql/javascript/ql/src/RegExp --format=csv --output=$host-$(date "+%Y.%m.%d-%H.%M.%S").csv -j $2
