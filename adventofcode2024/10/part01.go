package main

import (
	"strconv"
	"strings"
)

var positions = [4]cord{
	{-1, 0},
	{1, 0},
	{0, -1},
	{0, 1},
}

func checkNeighbor(curNum int, curPos cord, arr [][]int, dims cord, reachedNines map[cord]bool) {
	if curNum == 9 {
		reachedNines[curPos] = true
		return
	}

	for _, pos := range positions {

		newPos := cord{curPos.x + pos.x, curPos.y + pos.y}

		if checkValid(newPos, dims) && arr[newPos.y][newPos.x] == curNum+1 {
			checkNeighbor(
				curNum+1, newPos, arr, dims, reachedNines,
			)
		}

	}

}

func part01(input string) int {
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
				reachedNines := map[cord]bool{}
				checkNeighbor(num, pos, arr, dims, reachedNines)
				total += len(reachedNines)
			}
		}
	}

	return total
}
