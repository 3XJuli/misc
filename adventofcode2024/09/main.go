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

type cord struct {
	x, y int
}

func checkValid(checkCord cord, dims cord) bool {
	return checkCord.x >= 0 && checkCord.x < dims.x && checkCord.y >= 0 && checkCord.y < dims.y
}

//go:embed input
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
