package main

import (
	"strconv"
	"strings"
)

func checkNeighbor2(curNum int, curPos cord, arr [][]int, dims cord) int {
	if curNum == 9 {
		return 1
	}

	sum := 0
	for _, pos := range positions {

		newPos := cord{curPos.x + pos.x, curPos.y + pos.y}

		if checkValid(newPos, dims) && arr[newPos.y][newPos.x] == curNum+1 {
			sum += checkNeighbor2(
				curNum+1, newPos, arr, dims,
			)
		}

	}

	return sum

}

func part02(input string) int {
	lines := strings.Split(input, "\n")

	total := 0

	var arr [][]int = make([][]int, len(lines))

	for i, line := range lines {
		trLine := strings.TrimSpace(line)

		arr[i] = make([]int, len(trLine))

		for j, ch := range trLine {

			num, err := strconv.Atoi(string(ch))

			check(err)
			arr[i][j] = num
		}
	}

	dims := cord{len(arr[0]), len(arr)}

	for y, row := range arr {
		for x, num := range row {
			pos := cord{x, y}
			if num == 0 {
				total += checkNeighbor2(num, pos, arr, dims)
			}
		}
	}

	return total
}
