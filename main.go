package main

import (
	"fmt"

	gowiki "github.com/trietmn/go-wiki"
)

func main() {
	// Search for the Wikipedia page title
	search_result, _, err := gowiki.Search("Why is the sky blue", 3, false)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Printf("This is your search result: %v\n", search_result)

	// Get the page
	page, err := gowiki.GetPage("Rafael Nadal", -1, false, true)
	if err != nil {
		fmt.Println(err)
	}

	// Get the content of the page
	content, err := page.GetHTML()
	if err != nil {
		fmt.Println(err)
	}
	println(content)

	links, err := page.GetLink()
	if err != nil {
		fmt.Println(err)
	}
	println(links)
}
