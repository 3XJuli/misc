package main

import (
	"fmt"
	"strings"
)

type State struct {
	pos, direction coordinatePair
}

func checkLoop(state State, puzzleMap [][]int, startLocation coordinatePair) bool {

	newObstacle := coordinatePair{state.pos.x + state.direction.x, state.pos.y + state.direction.y}

	if newObstacle == startLocation {
		return false
	}

	visitedStates := map[State]bool{state: true}

	currDirection := state.direction
	currLocation := state.pos
	for true {
		newLocation := coordinatePair{currLocation.x + currDirection.x, currLocation.y + currDirection.y}
		// fmt.Println("Pos:", currLocation, "Dir: ", currDirection)

		if newLocation.y >= len(puzzleMap) || newLocation.y < 0 || newLocation.x < 0 || newLocation.x >= len(puzzleMap[newLocation.y]) {
			break
		} else if (puzzleMap[newLocation.y][newLocation.x] == 1) || ((newLocation.x == newObstacle.x) && (newLocation.y == newObstacle.y)) {
			currDirection = turnRight(currDirection)
			// fmt.Println("New Direction: ", currDirection)
		} else {
			currLocation = newLocation
			// fmt.Println("New Location: ", currLocation)
		}

		newState := State{currLocation, currDirection}
		_, ok := visitedStates[newState]
		if ok {
			// fmt.Println("Valid Obstacle:", newObstacle)
			return true
		} else {
			visitedStates[newState] = true
		}
	}

	return false

}

func part02(input string) int {

	splitInput := strings.Split(input, "\n")

	puzzleMap := make([][]int, len(splitInput))

	uniqueLocations := 0

	visitedState := map[State]bool{}

	var currLocation coordinatePair
	var startLocation coordinatePair

	currDirection := coordinatePair{0, -1}

	for i, line := range splitInput {
		puzzleMap[i] = make([]int, len(line))
		for j, char := range line {
			if char == '#' {
				puzzleMap[i][j] = 1
			} else if char == '^' {
				puzzleMap[i][j] = 0
				currLocation = coordinatePair{j, i}
				startLocation = coordinatePair{j, i}
			} else {
				puzzleMap[i][j] = 0
			}
		}
	}

	for true {
		newLocation := coordinatePair{currLocation.x + currDirection.x, currLocation.y + currDirection.y}

		if newLocation.y >= len(puzzleMap) || newLocation.y < 0 || newLocation.x < 0 || newLocation.x >= len(puzzleMap[newLocation.y]) {
			break
		} else {
			if puzzleMap[newLocation.y][newLocation.x] == 1 {
				currDirection = turnRight(currDirection)
			} else {
				currLocation = newLocation
			}
		}

		currState := State{
			currLocation, currDirection,
		}

		_, ok := visitedState[currState]
		if !ok {
			visitedState[currState] = true
			if checkLoop(currState, puzzleMap, startLocation) {
				fmt.Println(currState.pos)
				uniqueLocations += 1

			}
		}
	}

	return uniqueLocations

}
