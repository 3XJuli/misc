package main

import (
	"fmt"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type coordinatePair struct {
	x, y int
}

func turnRight(direction coordinatePair) coordinatePair {
	return coordinatePair{-direction.y, direction.x}
}

func part01(input string) int {

	splitInput := strings.Split(input, "\n")

	puzzleMap := make([][]int, len(splitInput))

	uniqueLocations := 0

	visitedLocations := map[coordinatePair]bool{}

	var currLocation coordinatePair

	currDirection := coordinatePair{0, -1}

	for i, line := range splitInput {
		puzzleMap[i] = make([]int, len(line))
		for j, char := range line {
			if char == '#' {
				puzzleMap[i][j] = 1
			} else if char == '^' {
				puzzleMap[i][j] = 0
				currLocation = coordinatePair{j, i}
				visitedLocations[currLocation] = true
				uniqueLocations += 1
			} else {
				puzzleMap[i][j] = 0
			}
		}
	}

	for true {
		newLocation := coordinatePair{currLocation.x + currDirection.x, currLocation.y + currDirection.y}
		fmt.Println("Pos:", currLocation, "New Pos:", newLocation, "Dir: ", currDirection)

		if newLocation.y >= len(puzzleMap) || newLocation.y < 0 || newLocation.x < 0 || newLocation.x >= len(puzzleMap[newLocation.y]) {
			break
		} else if puzzleMap[newLocation.y][newLocation.x] == 1 {
			currDirection = turnRight(currDirection)
		} else {
			_, ok := visitedLocations[newLocation]
			if !ok {
				visitedLocations[newLocation] = true
				uniqueLocations += 1
			}
			currLocation = newLocation
		}
	}

	return uniqueLocations

}
