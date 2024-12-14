package main

import (
	"image"
	"image/color"
	"log"
	"os"
	"path/filepath"
	"regexp"
	"strconv"
	"strings"

	"golang.org/x/image/bmp"
)

func logImage(t int, robots []*robot, dimx int, dimy int) {
	robotCoordinates := make(map[cord]bool)

	for _, robot := range robots {
		robotCoordinates[cord{robot.px, robot.py}] = true
	}

	im := image.NewGray(image.Rectangle{image.Point{0, 0}, image.Point{dimx, dimy}})

	for y := 0; y < dimy; y++ {
		for x := 0; x < dimx; x++ {
			_, ok := robotCoordinates[cord{x, y}]

			if ok {
				im.SetGray(x, y, color.Gray{255})
			}
		}
	}

	file := filepath.Join("debug", "file_"+strconv.Itoa(t)+".bmp")
	createdFile, err := os.Create(file)
	check(err)

	bmp.Encode(createdFile, im)
}

func part02(input string) int {
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

	t := 10000

	for i := 0; i < t; i++ {
		for _, robot := range robots {
			newx := (robot.px + robot.vx) % (dimx)
			newy := (robot.py + robot.vy) % (dimy)

			if newx < 0 {
				newx = dimx + newx
			}
			if newy < 0 {
				newy = dimy + newy
			}

			robot.px = newx
			robot.py = newy
		}

		logImage(
			i, robots, dimx, dimy,
		)
	}

	return -1

}
