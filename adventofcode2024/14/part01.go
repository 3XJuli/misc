package main

import (
	"log"
	"regexp"
	"strconv"
	"strings"
)

type robot struct {
	px, py, vx, vy int
}

func part01(input string) int {
	spString := strings.Split(input, "\n")

	robots := make([]*robot, 0)

	re := regexp.MustCompile(`[-]?[0-9]+`)
	for _, line := range spString {

		clLine := strings.TrimSpace(line)

		nums := re.FindAllString(clLine, 4)

		if len(nums) != 4 {
			log.Fatal("Invalid number found")
		}

		intNums := make([]int, 4)

		for i, num := range nums {
			intNum, err := strconv.Atoi(num)
			check(err)
			intNums[i] = intNum
		}

		robots = append(robots, &robot{intNums[0], intNums[1], intNums[2], intNums[3]})
	}

	dimx := 101
	dimy := 103

	quadrants := make([]int, 4)
	t := 100

	for _, robot := range robots {
		newx := (robot.px + t*robot.vx) % (dimx)
		newy := (robot.py + t*robot.vy) % (dimy)

		if newx < 0 {
			newx = dimx + newx
		}
		if newy < 0 {
			newy = dimy + newy
		}

		if newx < dimx/2 && newy < dimy/2 {
			quadrants[0] += 1
		} else if newx > dimx/2 && newy < dimy/2 {
			quadrants[1] += 1
		} else if newx < dimx/2 && newy > dimy/2 {
			quadrants[2] += 1
		} else if newx > dimx/2 && newy > dimy/2 {
			quadrants[3] += 1
		}
	}

	total := 1

	for _, quadrant := range quadrants {
		total *= quadrant
	}

	return total

}
