package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

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

	hLeft := &IntHeap{}
	hRight := &IntHeap{}

	heap.Init(hLeft)
	heap.Init(hRight)

	for scanner.Scan() {
		line := scanner.Text()

		splitString := strings.SplitN(line, "   ", 2)

		if len(splitString) != 2 {
			log.Fatal("Invalid input: ", line)
		}

		leftInt, err := strconv.Atoi(splitString[0])
		check(err)

		rightInt, err := strconv.Atoi(splitString[1])
		check(err)

		heap.Push(hLeft, leftInt)
		heap.Push(hRight, rightInt)

	}

	diffSum := 0

	for hLeft.Len() > 0 {
		leftInt := heap.Pop(hLeft).(int)
		rightInt := heap.Pop(hRight).(int)

		diffSum += absoluteDiff(leftInt, rightInt)
	}

	fmt.Printf("Diff Sum: %d\n", diffSum)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return diffSum
}
