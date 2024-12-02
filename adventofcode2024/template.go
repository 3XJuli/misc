package main

import (
	// "bufio"
	"fmt"
	// "io"
	"os"
)

var inputFilePath string = "input"

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	dat, err := os.ReadFile(inputFilePath)
	check(err)

	fmt.Println(string(dat))
}