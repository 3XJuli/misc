package main

import (
	"fmt"
	"strings"
)

type cord struct {
	x, y int
}

func checkValid(checkCord cord, dims cord) bool {
	return checkCord.x >= 0 && checkCord.x < dims.x && checkCord.y >= 0 && checkCord.y < dims.y

}

func part01(input string) int {

	var antennaMap map[rune][]cord = make(map[rune][]cord)

	spInp := strings.Split(input, "\n")

	antiNodes := make(map[cord]bool)

	dims := cord{len(strings.TrimSpace(spInp[0])), len(spInp)}

	for i, line := range spInp {

		for j, ch := range strings.TrimSpace(line) {
			if ch != '.' {
				antennaMap[ch] = append(antennaMap[ch], cord{j, i})
			}
		}
	}

	for _, cords := range antennaMap {
		for k, cordA := range cords {
			for l := k + 1; l < len(cords); l++ {
				cordB := cords[l]

				cordDiff := cord{cordB.x - cordA.x, cordB.y - cordA.y}

				// cordA - cordDiff
				// cordA + 2*cordDiff

				checkCordA := cord{cordA.x - cordDiff.x, cordA.y - cordDiff.y}
				checkCordB := cord{cordA.x + 2*cordDiff.x, cordA.y + 2*cordDiff.y}

				if checkValid(checkCordA, dims) {
					antiNodes[checkCordA] = true
				}
				if checkValid(checkCordB, dims) {
					antiNodes[checkCordB] = true
				}

			}
		}
	}

	for k := range antiNodes {
		fmt.Print(k)
	}

	return len(antiNodes)

}
