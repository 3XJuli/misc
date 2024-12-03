package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

func part02(input string) int {

	total := 0

	re := regexp.MustCompile(`mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)`)

	reNum := regexp.MustCompile(`[0-9]{1,3}`)

	do := true

	allMatches := re.FindAllString(input, -1)

	for _, match := range allMatches {

		if strings.HasPrefix(match, "don't") {
			do = false
		} else if strings.HasPrefix(match, "do") {
			do = true
		} else {
			if !do {
				continue
			}
			numbers := reNum.FindAllString(match, -1)

			numberA, err := strconv.Atoi(numbers[0])
			check(err)

			numberB, err := strconv.Atoi(numbers[1])
			check(err)

			total += numberA * numberB
		}

	}

	fmt.Println(allMatches)

	return total

}
