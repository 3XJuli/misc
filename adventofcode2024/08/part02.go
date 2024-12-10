package main

import "strings"

func part02(input string) int {
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

				i := 0
				for {
					checkCord := cord{cordA.x + i*cordDiff.x, cordA.y + i*cordDiff.y}

					if !checkValid(checkCord, dims) {
						break
					}

					antiNodes[checkCord] = true
					i += 1
				}
				i = -1
				for {
					checkCord := cord{cordA.x + i*cordDiff.x, cordA.y + i*cordDiff.y}

					if !checkValid(checkCord, dims) {
						break
					}

					antiNodes[checkCord] = true
					i -= 1
				}

			}
		}
	}

	return len(antiNodes)

}
