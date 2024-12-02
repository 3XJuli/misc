package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

type Pair struct {
	left, right int
}

func part02(input string) int {
	file, err := os.Open(inputFilePath)
	check(err)

	defer file.Close()

	var m map[int]*Pair = make(map[int]*Pair)

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()

		splitString := strings.SplitN(line, "   ", 2)

		if len(splitString) != 2 {
			log.Fatal("Invalid input: ", line)
		}

		leftInt, err := strconv.Atoi(splitString[0])
		check(err)

		pair, ok := m[leftInt]

		if ok {
			pair.left += 1
		} else {
			m[leftInt] = &Pair{left: 1, right: 0}
		}

		rightInt, err := strconv.Atoi(splitString[1])
		check(err)

		pair, ok = m[rightInt]
		if ok {
			pair.right += 1
		} else {
			m[rightInt] = &Pair{left: 0, right: 1}
		}

	}

	similarity := 0
	for key, value := range m {
		similarity += key * (value.left * value.right)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)

	}

	return similarity
}
