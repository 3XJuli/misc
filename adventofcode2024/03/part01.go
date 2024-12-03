package main

import (
	"fmt"
	"regexp"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func part01(input string) int {

	total := 0

	re := regexp.MustCompile(`mul\([0-9]{1,3},[0-9]{1,3}\)`)

	reNum := regexp.MustCompile(`[0-9]{1,3}`)

	allMatches := re.FindAllString(input, -1)

	for _, match := range allMatches {
		numbers := reNum.FindAllString(match, -1)

		numberA, err := strconv.Atoi(numbers[0])
		check(err)

		numberB, err := strconv.Atoi(numbers[1])
		check(err)

		total += numberA * numberB

	}

	fmt.Println(allMatches)

	return total

}
