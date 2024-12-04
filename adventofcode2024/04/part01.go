package main

import (
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

var directions = [8][2]int{
	{1, 0},
	{1, 1},
	{0, 1},
	{-1, 1},
	{-1, 0},
	{0, -1},
	{-1, -1},
	{1, -1},
}

const searchString = "MAS"

func checkDirection(input []string, currLoc [2]int, currChar int, direction [2]int) bool {
	if currChar > 2 {
		return true
	}
	// check we are in the input array
	if currLoc[0] == len(input) || currLoc[0] < 0 || currLoc[1] == len(input[0]) || currLoc[1] < 0 {
		return false
	}

	if input[currLoc[0]][currLoc[1]] == searchString[currChar] {
		return checkDirection(input, [2]int{currLoc[0] + direction[0], currLoc[1] + direction[1]}, currChar+1, direction)
	}

	return false
}

func part01(input string) int {

	splitInput := strings.Split(input, "\n")

	xMasCount := 0

	for i, line := range splitInput {
		for j, char := range line {
			if char == 'X' {
				for _, direction := range directions {
					if checkDirection(splitInput, [2]int{i + direction[0], j + direction[1]}, 0, direction) {
						xMasCount += 1
					}
				}
			}
		}
	}

	return xMasCount

}
