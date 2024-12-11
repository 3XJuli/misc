package main

import (
	"slices"
	"strconv"
	"strings"
)

func part01(input string) int {
	str := strings.TrimSpace(input)

	spStr := strings.Split(str, " ")

	curStones := make([]int, len(spStr))

	for i, st := range spStr {
		num, err := strconv.Atoi(st)
		check(err)
		curStones[i] = num
	}
	n := 25

	for i := 0; i < n; i++ {
		for j := 0; j < len(curStones); j++ {
			if curStones[j] == 0 {
				curStones[j] = 1
			} else {
				stoneString := strconv.Itoa(curStones[j])
				if len(stoneString)%2 == 0 {
					leftStone, err := strconv.Atoi(stoneString[:len(stoneString)/2])
					check(err)

					rightStone, err := strconv.Atoi(stoneString[len(stoneString)/2:])
					check(err)

					curStones[j] = leftStone
					curStones = slices.Insert(curStones, j+1, rightStone)

					j += 1
				} else {
					curStones[j] *= 2024
				}
			}
		}
	}

	return len(curStones)
}
