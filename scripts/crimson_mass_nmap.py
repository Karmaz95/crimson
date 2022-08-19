import nmap
import json
nm = nmap.PortScanner()

all_services = []
scan_results = []
output_csv = []
i = 0

with open("all.txt") as f:
    for line in f:
        print("Ip pair number [" + str(i) + "] " + line.rstrip()) # Scan progress
        splited_line = line.rstrip().split(":")
        ip = splited_line[0]
        port = splited_line[1]
        #all_services.append(splited_line) # array with all ip:port pairs # print all_services[1]
        
        scan_results.append(nm.scan(ip,port, arguments="-Pn -A"))
        print("------- Scan info: ")
        print(json.dumps(scan_results[i], sort_keys=True, indent=4))
        print("------- Output csv:")
        print(nm.csv())
        output_csv.append(nm.csv())
        i+=1

# Filtered output in csv format:
final_list = ["host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe"]
for element in output_csv:
    s = element.split("\n")[1].rstrip()
    final_list.append(s)
    print(s)

f = open("output_csv.txt", "a")
for element in final_list:
    f.write(element + "\n")

f.close()


# Full scan list for debugging purpose
f = open("scan_results.txt", "a")
f.write(str(scan_results))
f.close()
