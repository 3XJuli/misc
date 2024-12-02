package main

import (
	"bufio"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

var inputFilePath string = "input"

func absoluteDiff(a, b int) int {
	return int(math.Abs(float64(a - b)))
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func part01(input string) int {
	file, err := os.Open(inputFilePath)
	check(err)

	defer file.Close()

	scanner := bufio.NewScanner(file)

	safeReports := 0

	for scanner.Scan() {
		line := scanner.Text()

		splitString := strings.Split(line, " ")

		firstNumber, err := strconv.Atoi(splitString[0])
		check(err)

		decreasing := false

		secondNumber, err := strconv.Atoi(splitString[1])
		check(err)

		if firstNumber > secondNumber {
			decreasing = true
		}

		safeReport := true

		prevInt := firstNumber
		for i := 1; i < len(splitString); i++ {
			newInt, err := strconv.Atoi(splitString[i])
			check(err)

			if decreasing && newInt >= prevInt {
				safeReport = false
				break
			} else if !decreasing && newInt <= prevInt {
				safeReport = false
				break
			}

			absDiff := absoluteDiff(newInt, prevInt)

			if (absDiff < 1) || (absDiff > 3) {
				safeReport = false
				break
			}

			prevInt = newInt
		}

		if safeReport {
			safeReports += 1
		}

	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return safeReports
}
