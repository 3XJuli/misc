package main

import (
	"fmt"
	"slices"
	"strings"
)

type side struct {
	direction cord
	axis      int
}

type plot2 struct {
	symbol string
	area   int
	sides  map[side][]int
}

func explorePlot2(pos cord, p *plot2, arr [][]symbolState, dims cord) {
	p.area += 1
	arr[pos.y][pos.x].visited = true

	for _, direction := range directions {
		newPos := cord{pos.x + direction.x, pos.y + direction.y}

		var relSide side
		var contCheck int

		if direction.x == 0 {
			relSide = side{direction, newPos.y}
			contCheck = newPos.x
		} else {
			relSide = side{direction, newPos.x}
			contCheck = newPos.y
		}

		if checkValid(newPos, dims) {
			newState := arr[newPos.y][newPos.x]
			if newState.symbol == p.symbol {
				if !newState.visited {
					explorePlot2(newPos, p, arr, dims)
				}
			} else {
				_, ok := p.sides[relSide]

				if !ok {
					p.sides[relSide] = make([]int, 0)
				}

				p.sides[relSide] = append(p.sides[relSide], contCheck)
			}
		} else {
			_, ok := p.sides[relSide]

			if !ok {
				p.sides[relSide] = make([]int, 0)
			}

			p.sides[relSide] = append(p.sides[relSide], contCheck)
		}
	}

}

func part02(input string) int {

	trInput := strings.Split(input, "\n")

	var arr [][]symbolState = make([][]symbolState, len(trInput))

	for y, line := range trInput {
		trLine := strings.TrimSpace(line)
		arr[y] = make([]symbolState, len(trLine))
		for x, ch := range trLine {
			arr[y][x] = symbolState{string(ch), false}
		}
	}

	plots := []plot2{}

	dims := cord{len(arr[0]), len(arr)}

	for y, line := range arr {
		for x, state := range line {
			if !state.visited {
				newPlot := plot2{
					state.symbol, 0, make(map[side][]int),
				}

				pos := cord{x, y}

				explorePlot2(pos, &newPlot, arr, dims)

				plots = append(plots, newPlot)
			}
		}
	}

	total := 0
	for _, plot := range plots {

		fmt.Println("Plot: ", plot)

		contSideCnt := 0
		for side, contCheck := range plot.sides {
			fmt.Println(side)
			contSideCnt += 1
			slices.Sort(contCheck)

			for j := 1; j < len(contCheck); j++ {
				if contCheck[j-1]+1 != contCheck[j] {
					contSideCnt += 1
				}
			}

		}
		total += plot.area * contSideCnt
	}
	return total
}
