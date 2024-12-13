package main

import (
	"regexp"
	"strconv"
	"strings"
)

func part02(input string) int {
	spString := strings.Split(input, "\n")

	re := regexp.MustCompile(`[0-9]+`)

	total := 0

	var ax, ay, bx, by, zx, zy float64
	for i, line := range spString {

		clLine := strings.TrimSpace(line)

		nums := re.FindAllString(clLine, 2)

		if i%4 == 3 {
			nb := (zy*ax - zx*ay) / (-bx*ay + ax*by)
			na := (zx - nb*bx) / ax

			if nb == float64(int64(nb)) && na == float64(int64(na)) {
				total += 3*int(na) + int(nb)
			}

			continue

		}

		num1, err := strconv.Atoi(nums[0])
		check(err)

		num2, err := strconv.Atoi(nums[1])
		check(err)
		if i%4 == 0 {
			ax, ay = float64(num1), float64(num2)
		} else if i%4 == 1 {
			bx, by = float64(num1), float64(num2)

		} else if i%4 == 2 {
			zx, zy = float64(num1+10000000000000), float64(num2+10000000000000)
		}
	}

	return total
}
