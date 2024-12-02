package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

func checkSafe(splitString []string) bool {

	firstNumber, err := strconv.Atoi(splitString[0])
	check(err)

	decreasing := false

	secondNumber, err := strconv.Atoi(splitString[1])
	check(err)

	if firstNumber > secondNumber {
		decreasing = true
	}

	prevInt := firstNumber
	safeReport := true
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

	return safeReport
}

func part02(input string) int {
	file, err := os.Open(inputFilePath)
	check(err)

	defer file.Close()

	scanner := bufio.NewScanner(file)

	safeReports := 0

	ix := 0

	for scanner.Scan() {
		line := scanner.Text()

		splitString := strings.Split(line, " ")
		safeReport := false
		for i := 0; i < len(splitString); i++ {

			checkString := slices.Concat(splitString[:i], splitString[i+1:])

			if checkSafe(checkString) {
				safeReport = true
				break
			}
		}

		if safeReport {
			fmt.Println("Safe line ", ix, ": ", splitString)
			safeReports += 1
		} else {
			fmt.Println("Unsafe line: ", ix, ": ", splitString)
		}

		ix += 1

	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return safeReports
}
