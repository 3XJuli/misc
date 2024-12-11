package main

import (
	"slices"
	"strconv"
	"strings"
)

func sortByOrder(a int, b int) int {
	aOrd, ok := intOrder[a]

	if !ok {
		return 0
	}

	_, before := aOrd.before[b]

	if before {
		return -1
	}

	_, after := aOrd.after[b]

	if after {
		return 1
	}

	return 0

}

func part02(input string) int {

	splitInput := strings.Split(input, "\n")

	total := 0

	lineIx := 0

	for _, line := range splitInput {
		lineIx += 1
		if len(line) == 0 {
			break
		}

		lineSplits := strings.Split(line, "|")

		leftInt, err := strconv.Atoi(lineSplits[0])
		check(err)
		rightInt, err := strconv.Atoi(lineSplits[1])
		check(err)

		ord, ok := intOrder[leftInt]

		if ok {
			ord.before[rightInt] = true
		} else {
			intOrder[leftInt] = &Order{before: map[int]bool{rightInt: true}, after: map[int]bool{}}
		}

		ord, ok = intOrder[rightInt]
		if ok {
			ord.after[leftInt] = true
		} else {
			intOrder[rightInt] = &Order{before: map[int]bool{}, after: map[int]bool{leftInt: true}}
		}

	}

	for i := lineIx; i < len(splitInput); i++ {
		splitLine := strings.Split(splitInput[i], ",")
		var visited map[int]bool = make(map[int]bool)
		// var numbers []int = make([]int, len(splitLine))

		lineValid := true

		var numbers []int

		for _, numberStr := range splitLine {
			num, err := strconv.Atoi(numberStr)
			check(err)

			numbers = append(numbers, num)
		}

		for j := 0; j < len(numbers)-1; j++ {
			num := numbers[j]

			ord, ok := intOrder[num]

			if !ok {
				visited[num] = true
				continue
			}

			for k := j + 1; k < len(numbers); k++ {
				_, ok := ord.after[numbers[k]]

				if ok {
					_, ok := visited[numbers[k]]

					if !ok {
						lineValid = false
						break
					}
				}

			}

			if !lineValid {
				break
			}
		}

		if !lineValid {

			slices.SortFunc(numbers, sortByOrder)

			middleNum := numbers[len(numbers)/2]
			total += middleNum
		}

	}

	return total

}