package main

import (
	"strings"
)

const ms = "MS"

func checkDirectionMAS(input []string, currLoc [2]int, char int) bool {
	if currLoc[0] == len(input) || currLoc[0] < 0 || currLoc[1] == len(input[0]) || currLoc[1] < 0 {
		return false
	}

	if input[currLoc[0]][currLoc[1]] == ms[char] {
		return true
	}
	return false
}

func part02(input string) int {

	splitInput := strings.Split(input, "\n")

	xMasCount := 0

	for i, line := range splitInput {
		for j, char := range line {
			if char == 'A' {
				if ((checkDirectionMAS(
					splitInput, [2]int{i - 1, j - 1}, 0,
				) && checkDirectionMAS(
					splitInput, [2]int{i + 1, j + 1}, 1,
				)) || (checkDirectionMAS(
					splitInput, [2]int{i - 1, j - 1}, 1,
				) && checkDirectionMAS(
					splitInput, [2]int{i + 1, j + 1}, 0,
				))) && ((checkDirectionMAS(
					splitInput, [2]int{i - 1, j + 1}, 0,
				) && checkDirectionMAS(
					splitInput, [2]int{i + 1, j - 1}, 1,
				)) || (checkDirectionMAS(
					splitInput, [2]int{i - 1, j + 1}, 1,
				) && checkDirectionMAS(
					splitInput, [2]int{i + 1, j - 1}, 0,
				))) {
					xMasCount += 1
				}

			}
		}
	}

	return xMasCount

}
