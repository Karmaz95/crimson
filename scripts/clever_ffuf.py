# THIS IS ADDON TO CRIMSON_TARGET
#
### CREATED BY KARMAZ
#
#
# FUNCTIONS:
#
# 1. Read the ffuf_status.txt
# 2. Count all responses
# 3. Count responses per status code
# 4. Check the rules.
# 5. Rules:
#       - Total count per status code cannot be bigger than 90% of all.
#       - If the total count is bigger than 70 % merge all into one.
#    
###
import re, os

# GET THE TARGET DOMAIN
target_domain = os.getenv("domain")
print(target_domain)

# ARRAYS WITH LINES OF STATUS CODE
status_all = []
status_200 = []
status_301 = []
status_302 = []
status_401 = []
status_403 = []
status_404 = []
status_odd = []
final_list = []

### LOOP THROUGH FUFF FILE AND COUNT STUFF
my_file = open("status_ffuf.txt", "r")
for line in my_file:
    status_all.append(line.rstrip().split("\"")[3])
    if "\"status\":200" in line:
        status_200.append(line.rstrip().split("\"")[3])
    elif "\"status\":301" in line:
        status_301.append(line.rstrip().split("\"")[3])
    elif "\"status\":302" in line:
        status_302.append(line.rstrip().split("\"")[3])
    elif "\"status\":401" in line:
        status_401.append(line.rstrip().split("\"")[3])
    elif "\"status\":403" in line:
        status_403.append(line.rstrip().split("\"")[3])
    elif "\"status\":404" in line:
        status_404.append(line.rstrip().split("\"")[3])
    else:
        status_odd.append(line.rstrip().split("\"")[3])

my_file.close()

### COUNTERS
status_all_c = len(status_all)
status_200_c = len(status_200)
status_301_c = len(status_301)
status_302_c = len(status_302)
status_401_c = len(status_401)
status_403_c = len(status_403)
status_404_c = len(status_404)
status_odd_c = len(status_odd)

### PRINT RESULTS
print(" DIR BRUTE STATUS ")
print(" ---------------- ")
print(" TOTAL   : " + str(status_all_c))
print(" 200     : " + str(status_200_c) + " (" + str(round((status_200_c / status_all_c),3)) + "%)")
print(" 301     : " + str(status_301_c) + " (" + str(round((status_301_c / status_all_c),3)) + "%)")
print(" 302     : " + str(status_302_c) + " (" + str(round((status_302_c / status_all_c),3)) + "%)")
print(" 401     : " + str(status_401_c) + " (" + str(round((status_401_c / status_all_c),3)) + "%)")
print(" 403     : " + str(status_403_c) + " (" + str(round((status_403_c / status_all_c),3)) + "%)")
print(" 404     : " + str(status_404_c) + " (" + str(round((status_404_c / status_all_c),3)) + "%)")
print(" OTHER   : " + str(status_odd_c) + " (" + str(round((status_odd_c / status_all_c),3)) + "%)")
print(" ---------------- ")

### MAIN FUNCTIONALITY
if (status_200_c / status_all_c) < 0.3:   
    final_list.extend(status_200)
if (status_301_c / status_all_c) < 0.001:
    final_list.extend(status_301)
if (status_302_c / status_all_c) < 0.001:
    final_list.extend(status_302)
if (status_401_c / status_all_c) < 0.001:
    final_list.extend(status_401)
if (status_403_c / status_all_c) < 0.001:
    final_list.extend(status_403)
if (status_404_c / status_all_c) < 0.001:
    final_list.extend(status_404)
final_list.extend(status_odd)

### SAVE THE OUTPUT TO A FILE => temp_ffuf.txt
output_file = open("temp_ffuf.txt","w")
for line in final_list:
    output_file.write("https://" + target_domain + "/" + line + "\n")

output_file.close()


'''
import re
from collections import Counter

c = Counter()
with open("status_ffuf.txt", "r") as my_file:
    sep = ' '
    without_first = [sep.join(line.split(sep)[1:]).strip() for line in my_file.readlines()]
    c = Counter(without_first)
    result = {}
    for key, count in c.items():
        print(key.strip(), count)
        result[re.search(r"Status: (\d{3})", key).group(1)] = count
    print(result)
'''
