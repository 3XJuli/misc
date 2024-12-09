package main

import (
	"adventofcode/util"
	_ "embed"
	"flag"
	"fmt"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

//go:embed debug_input
var input string

func main() {
	var part int
	flag.IntVar(&part, "part", 1, "part 1 or part 2")

	flag.Parse()

	fmt.Println("Running Part", part)

	var ans int

	if part == 1 {
		ans = part01(input)
	} else {
		ans = part02(input)
	}
	err := util.CopyToClipboard(fmt.Sprintf("%v", ans))

	check(err)

	fmt.Println("Output (copied to clipboard):", ans)
}
