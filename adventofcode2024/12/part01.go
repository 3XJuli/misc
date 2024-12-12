package main

import "strings"

type symbolState struct {
	symbol  string
	visited bool
}

type plot struct {
	symbol    string
	area      int
	perimeter int
}

var directions = [4]cord{
	{-1, 0},
	{1, 0},
	{0, -1},
	{0, 1},
}

func explorePlot(pos cord, p *plot, arr [][]symbolState, dims cord) {
	p.area += 1
	arr[pos.y][pos.x].visited = true

	for _, direction := range directions {
		newPos := cord{pos.x + direction.x, pos.y + direction.y}

		if checkValid(newPos, dims) {
			newState := arr[newPos.y][newPos.x]
			if newState.symbol == p.symbol {
				if !newState.visited {
					explorePlot(newPos, p, arr, dims)
				}
			} else {
				p.perimeter += 1
			}
		} else {
			p.perimeter += 1
		}
	}

}

func part01(input string) int {

	trInput := strings.Split(input, "\n")

	var arr [][]symbolState = make([][]symbolState, len(trInput))

	for y, line := range trInput {
		trLine := strings.TrimSpace(line)
		arr[y] = make([]symbolState, len(trLine))
		for x, ch := range trLine {
			arr[y][x] = symbolState{string(ch), false}
		}
	}

	plots := []plot{}

	dims := cord{len(arr[0]), len(arr)}

	for y, line := range arr {
		for x, state := range line {
			if !state.visited {
				newPlot := plot{
					state.symbol, 0, 0,
				}

				pos := cord{x, y}

				explorePlot(pos, &newPlot, arr, dims)

				plots = append(plots, newPlot)
			}
		}
	}

	total := 0

	for _, plot := range plots {
		total += plot.area * plot.perimeter
	}

	return total
}
