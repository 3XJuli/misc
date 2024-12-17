package main

import (
	"fmt"
	"strings"
)

func printArray2(arr [][]string) {
	fmt.Println()
	fmt.Println(strings.Repeat("#", len(arr[0])+2))
	for _, line := range arr {
		fmt.Println("#" + strings.Join(line, "") + "#")
	}
	fmt.Println(strings.Repeat("#", len(arr[0])+2))
}

func canMove(crate [2]cord, dir cord, arr [][]string, dims cord) bool {
	newPos1 := cord{crate[0].x, crate[0].y + dir.y}
	newPos2 := cord{crate[1].x, crate[1].y + dir.y}

	if !checkValid(newPos1, dims) || !checkValid(newPos2, dims) {
		return false
	}

	arrPos1 := arr[newPos1.y][newPos1.x]
	arrPos2 := arr[newPos2.y][newPos2.x]

	if arrPos1 == "#" || arrPos2 == "#" {
		return false
	} else if arrPos1 == "[" && arrPos2 == "]" {
		newCrate := [2]cord{newPos1, newPos2}
		return canMove(newCrate, dir, arr, dims)
	}

	var canMove1, canMove2 bool
	if arrPos1 == "." {
		canMove1 = true
	} else {
		newCrate := [2]cord{{newPos1.x - 1, newPos1.y}, newPos1}
		canMove1 = canMove(newCrate, dir, arr, dims)
	}

	if arrPos2 == "." {
		canMove2 = true
	} else {
		newCrate := [2]cord{newPos2, {newPos2.x + 1, newPos2.y}}
		canMove2 = canMove(newCrate, dir, arr, dims)
	}

	return canMove1 && canMove2
}

func move(crate [2]cord, dir cord, arr [][]string, dims cord) {
	newPos1 := cord{crate[0].x, crate[0].y + dir.y}
	newPos2 := cord{crate[1].x, crate[1].y + dir.y}

	if arr[newPos1.y][newPos1.x] == "[" && arr[newPos2.y][newPos2.x] == "]" {
		move([2]cord{newPos1, newPos2}, dir, arr, dims)
	} else {
		if arr[newPos1.y][newPos1.x] == "]" {
			move([2]cord{{newPos1.x - 1, newPos1.y}, newPos1}, dir, arr, dims)
		}
		if arr[newPos2.y][newPos2.x] == "[" {
			move([2]cord{newPos2, {newPos2.x + 1, newPos2.y}}, dir, arr, dims)
		}
	}

	arr[crate[0].y][crate[0].x] = "."
	arr[crate[1].y][crate[1].x] = "."
	arr[newPos1.y][newPos1.x] = "["
	arr[newPos2.y][newPos2.x] = "]"
}

func checkPos(
	pos cord, dir cord, arr [][]string, dims cord,
) bool {

	oldSymb := arr[pos.y][pos.x]
	newPos := cord{pos.x + dir.x, pos.y + dir.y}
	if !checkValid(newPos, dims) || arr[newPos.y][newPos.x] == "#" {
		return false
	}
	symb := arr[newPos.y][newPos.x]

	if symb == "." {
		arr[newPos.y][newPos.x] = oldSymb
		return true
	}

	if (dir == cord{-1, 0} || dir == cord{1, 0}) {
		if checkPos(newPos, dir, arr, dims) {
			arr[newPos.y][newPos.x] = oldSymb
			return true
		}
	} else {
		var crate [2]cord
		if symb == "[" {
			crate = [2]cord{newPos, {newPos.x + 1, newPos.y}}
		} else {
			crate = [2]cord{{newPos.x - 1, newPos.y}, newPos}
		}

		if canMove(crate, dir, arr, dims) {
			move(crate, dir, arr, dims)
			return true
		}
	}

	return false
}

func part02(input string) int {
	spInput := strings.Split(input, "\n")

	arr := make([][]string, 0)

	instructions := make([]cord, 0)

	fillArr := true

	var robotPos cord

	for i, line := range spInput {
		trLine := strings.TrimSpace(line)
		if trLine == "" {
			fillArr = false
			continue
		}

		if fillArr {
			if i == 0 || strings.TrimSpace(spInput[i+1]) == "" {
				continue
			}
			arr = append(arr, make([]string, 2*(len(trLine)-2)))
			for j := 1; j < (len(trLine) - 1); j++ {
				symbol := string(trLine[j])

				if symbol == "@" {
					arr[i-1][2*j-2] = "@"
					arr[i-1][2*j-1] = "."
					robotPos = cord{2*j - 2, i - 1}
				} else if symbol == "O" {
					arr[i-1][2*j-2] = "["
					arr[i-1][2*j-1] = "]"
				} else {
					arr[i-1][2*j-2] = symbol
					arr[i-1][2*j-1] = symbol
				}

			}
		} else {
			for _, ch := range trLine {
				symbol := string(ch)

				var dir cord
				if symbol == "<" {
					dir = directions[0]
				} else if symbol == ">" {
					dir = directions[1]
				} else if symbol == "^" {
					dir = directions[2]
				} else if symbol == "v" {
					dir = directions[3]
				}

				instructions = append(instructions, dir)
			}
		}
	}

	dims := cord{len(arr[0]), len(arr)}

	printArray(arr, nil)

	for _, instruction := range instructions {
		if checkPos(robotPos, instruction, arr, dims) {
			arr[robotPos.y][robotPos.x] = "."
			arr[robotPos.y+instruction.y][robotPos.x+instruction.x] = "@"
			robotPos = cord{robotPos.x + instruction.x, robotPos.y + instruction.y}
		}

		printArray(arr, &instruction)
	}

	total := 0

	for i, row := range arr {
		for j, val := range row {
			if val == "[" {
				total += 100*(i+1) + (j + 2)
			}
		}
	}

	return total
}
