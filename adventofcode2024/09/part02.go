package main

import (
	"fmt"
	"strconv"
	"strings"
)

type File struct {
	id, size int
}

func printMemory(files []File, buffers []int) {
	line := ""
	for i, file := range files {
		line += strings.Repeat(strconv.Itoa(file.id), file.size)

		if i < len(buffers) {
			line += strings.Repeat(".", buffers[i])
		}
	}

	fmt.Println(line)
}

func insertFile(files []File, file File, index int) []File {
	return append(files[:index], append([]File{file}, files[index:]...)...)
}
func insertInt(array []int, value int, index int) []int {
	return append(array[:index], append([]int{value}, array[index:]...)...)
}

func removeFile(files []File, index int) []File {
	return append(files[:index], files[index+1:]...)
}
func removeInt(array []int, index int) []int {
	return append(array[:index], array[index+1:]...)
}

func moveFile(files []File, srcIndex int, dstIndex int) []File {
	file := files[srcIndex]

	return insertFile(removeFile(files, srcIndex), file, dstIndex)
}

func calculateChecksum(files []File, buffers []int) int {
	checkSumIndex := 0
	checkSum := 0
	for i, file := range files {
		for j := 0; j < file.size; j++ {
			checkSum += (checkSumIndex + j) * file.id
		}
		checkSumIndex += buffers[i] + file.size
	}
	return checkSum
}

func part02(input string) int {

	total := 0

	strInput := strings.TrimSpace(input)
	files := make([]File, len(strInput)/2+1)
	buffers := make([]int, len(strInput)/2)

	for i, ch := range strInput {

		num, err := strconv.Atoi(string(ch))
		check(err)
		if i%2 == 0 {
			files[i/2] = File{i / 2, num}
		} else {
			buffers[i/2] = num
		}
	}
	printMemory(files, buffers)
	// bufferIndex := 0

	minFileId := 1000000000000000

	i := len(files) - 1
	for i >= 0 {

		file := files[i]
		if file.id > minFileId {
			i -= 1
			continue
		}

		minFileId = file.id

		fmt.Println("Checking file: ", file.id)

		foundBuffer := false

		for j := 0; j < i; j++ {

			if buffers[j] >= file.size {
				files = moveFile(files, i, j+1)
				// printMemory(files, buffers)
				newBufferSize := buffers[j] - file.size
				buffers[j] = 0
				// printMemory(files, buffers)

				buffers = insertInt(buffers, newBufferSize, j+1)
				buffers[i] += file.size
				if i+1 < len(buffers) {
					buffers[i] += buffers[i+1]
					removeInt(buffers, i+1)
				}
				// printMemory(files, buffers)

				foundBuffer = true

				break

			}

		}

		if !foundBuffer {
			i -= 1
		}
	}

	total = calculateChecksum(files, buffers)

	return total
}
