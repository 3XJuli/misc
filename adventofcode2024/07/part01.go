package main

import (
	"strconv"
	"strings"
)

func dfs(pos int, nums []int, curTotal int, total int) bool {
	if total == curTotal && pos == len(nums) {
		return true
	}

	if pos == len(nums) || curTotal > total {
		return false
	}

	concatenation, err := strconv.Atoi(strconv.Itoa(curTotal) + strconv.Itoa(nums[pos]))
	check(err)

	// Option 1: Add the current num
	// Option 2: Multiply the current num
	return dfs(pos+1, nums, curTotal+nums[pos], total) || dfs(pos+1, nums, curTotal*nums[pos], total) || dfs(pos+1, nums, concatenation, total)

}

func part01(input string) int {

	total := 0

	spInp := strings.Split(input, "\n")

	for _, line := range spInp {
		spLine := strings.Split(line, ": ")

		tot, err := strconv.Atoi(spLine[0])
		check(err)

		spNums := strings.Split(spLine[1], " ")

		var nums []int = make([]int, len(spNums))

		for ix, strNum := range spNums {
			num, err := strconv.Atoi(strNum)
			check(err)
			nums[ix] = num
		}

		if dfs(1, nums, nums[0], tot) {
			total += tot
		}

	}
	return total

}
