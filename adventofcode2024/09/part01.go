package main

import (
	"strconv"
	"strings"
)

func part01(input string) int {

	total := 0

	strInput := strings.TrimSpace(input)
	nums := make([]int, len(strInput))

	for i, ch := range strInput {
		num, err := strconv.Atoi(string(ch))
		check(err)
		nums[i] = num
	}

	blockPosition := 0
	leftCursor := 0
	rightCursor := len(nums) - 1
	leftId := -1
	rightId := len(nums) / 2

	for leftCursor <= rightCursor {
		leftNum := nums[leftCursor]
		rightNum := nums[rightCursor]

		if leftNum == 0 {
			leftCursor += 1
			continue
		}

		if rightNum == 0 {
			rightCursor -= 2
			rightId -= 1
			continue
		}

		if leftCursor%2 == 0 {
			leftId += 1
			for i := 0; i < leftNum; i++ {
				total += (blockPosition + i) * leftId
			}
			blockPosition += leftNum
			leftCursor += 1
			continue
		}

		if leftNum >= rightNum {
			for i := 0; i < rightNum; i++ {
				total += (blockPosition + i) * rightId
			}

			blockPosition += rightNum
			nums[leftCursor] -= rightNum
			nums[rightCursor] = 0
		} else {
			for i := 0; i < leftNum; i++ {
				total += (blockPosition + i) * rightId
			}
			blockPosition += leftNum
			nums[leftCursor] = 0
			nums[rightCursor] -= leftNum
		}

	}

	return total
}
