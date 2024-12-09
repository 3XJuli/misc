package main

import (
	"strings"
)

type coord struct {
	x, y int
}

func part01(input string) int {

	var antennaMap map[rune][]coord = make(map[rune][]coord)

	total := 0

	spInp := strings.Split(input, "\n")

	antiNodes := make(map[coord]bool)

	for i, line := range spInp {
		for j, ch := range line {
			antennaMap[ch] = append(antennaMap[ch], coord{j, i})
		}
	}

	for _, nums := range antennaMap {
		return 0
	}

	return total

}
