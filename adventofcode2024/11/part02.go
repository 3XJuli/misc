package main

import (
	"strconv"
	"strings"
)

func part02(input string) int {
	str := strings.TrimSpace(input)

	spStr := strings.Split(str, " ")

	// curStones := make([]int, len(spStr))

	curStones := map[int]int{}

	for _, st := range spStr {
		num, err := strconv.Atoi(st)
		check(err)
		curStones[num] += 1
	}
	n := 75

	for i := 0; i < n; i++ {
		newStones := map[int]int{}
		for stone, cnt := range curStones {
			if stone == 0 {
				newStones[1] += cnt
			} else {
				stoneString := strconv.Itoa(stone)
				if len(stoneString)%2 == 0 {
					leftStone, err := strconv.Atoi(stoneString[:len(stoneString)/2])
					check(err)

					rightStone, err := strconv.Atoi(stoneString[len(stoneString)/2:])
					check(err)

					newStones[leftStone] += cnt
					newStones[rightStone] += cnt
				} else {
					newStones[stone*2024] += cnt
				}
			}
		}
		curStones = newStones

	}
	total := 0
	for _, cnt := range curStones {
		total += cnt
	}

	return total
}
