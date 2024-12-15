package main

import (
	"fmt"
	"strings"
)

var directions = [4]cord{
	{-1, 0},
	{1, 0},
	{0, -1},
	{0, 1},
}

func printArray(arr [][]string) {
	fmt.Println()
	fmt.Println(strings.Repeat("#", len(arr[0])+2))
	for _, line := range arr {
		fmt.Println("#" + strings.Join(line, "") + "#")
	}
	fmt.Println(strings.Repeat("#", len(arr[0])+2))
}

func pushCrate(
	pos cord, dir cord, arr [][]string, dims cord,
) bool {
	newPos := cord{pos.x + dir.x, pos.y + dir.y}

	if !checkValid(newPos, dims) {
		return false
	}

	if arr[newPos.y][newPos.x] == "O" {
		if pushCrate(newPos, dir, arr, dims) {
			arr[newPos.y][newPos.x] = arr[pos.y][pos.x]

			return true
		}

		return false
	} else if arr[newPos.y][newPos.x] == "#" {
		return false
	} else {
		arr[newPos.y][newPos.x] = arr[pos.y][pos.x]
		return true
	}
}

func part01(input string) int {
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
			if i == 0 || spInput[i+1] == "" {
				continue
			}
			arr = append(arr, make([]string, len(trLine)-2))
			for j := 1; j < len(trLine)-1; j++ {
				symbol := string(trLine[j])

				if symbol == "@" {
					robotPos = cord{j - 1, i - 1}
				}

				arr[i-1][j-1] = symbol
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

	for _, instruction := range instructions {
		newCord := cord{robotPos.x + instruction.x, robotPos.y + instruction.y}

		if !checkValid(newCord, dims) || arr[newCord.y][newCord.x] == "#" {
			continue
		}

		if arr[newCord.y][newCord.x] == "O" {
			if pushCrate(newCord, instruction, arr, dims) {

				arr[robotPos.y][robotPos.x] = "."
				arr[newCord.y][newCord.x] = "@"
				robotPos = newCord

			}
		} else {
			arr[robotPos.y][robotPos.x] = "."
			arr[newCord.y][newCord.x] = "@"
			robotPos = newCord
		}

		printArray(arr)
	}

	total := 0

	for i, row := range arr {
		for j, val := range row {
			if val == "O" {
				total += 100*(i+1) + (j + 1)
			}
		}
	}

	return total
}
