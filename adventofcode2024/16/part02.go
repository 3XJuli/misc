package main

import (
	"container/heap"
	"fmt"
	"strings"
)

type SimpleSet struct {
	cords map[cord]bool
}

func (s *SimpleSet) Add(c cord) {
	s.cords[c] = true
}

func (s *SimpleSet) GetCopy() SimpleSet {
	newCords := make(map[cord]bool, len(s.cords))

	for k, _ := range s.cords {
		newCords[k] = true
	}

	return SimpleSet{newCords}
}

func (s *SimpleSet) Union(s2 *SimpleSet) SimpleSet {
	s3 := s.GetCopy()
	if s2 != nil {
		for k, _ := range s2.cords {
			s3.cords[k] = true
		}
	}
	return s3
}

func (s *SimpleSet) Len() int {
	return len(s.cords)
}

func printPath(arr [][]string, cords map[cord]bool) {
	for y, row := range arr {
		line := ""
		for x, ch := range row {
			_, ok := cords[cord{x, y}]
			if ok {
				line += "O"
			} else {
				line += ch
			}
		}

		fmt.Println(line)
	}
}

func part02(input string) int {
	spInput := strings.Split(input, "\n")

	visited := make(map[Node]*State)

	arr := make([][]string, len(spInput))

	var start cord
	var end cord

	for i, line := range spInput {
		trLine := strings.TrimSpace(line)

		arr[i] = make([]string, len(trLine))

		for j, ch := range trLine {
			arr[i][j] = string(ch)

			if string(ch) == "E" {
				end = cord{j, i}
			} else if string(ch) == "S" {
				start = cord{j, i}
			}
		}
	}

	initNode := Node{start, 2}

	pq := make(PriorityQueue, 1)

	initPathSet := SimpleSet{cords: map[cord]bool{start: true}}

	pq[0] = &State{initNode, initPathSet, 0, 0}

	visited[initNode] = pq[0]

	heap.Init(&pq)

	finalCost := 115500

	finalPaths := SimpleSet{cords: map[cord]bool{end: true}}

	for pq.Len() > 0 {
		state := heap.Pop(&pq).(*State)

		node := state.node
		path := state.pathSet
		dirIx := node.dir
		nodePos := node.pos

		fwPos := cord{nodePos.x + directions[dirIx].x, nodePos.y + directions[dirIx].y}

		if state.cost+1 > finalCost {
			break
		}

		if fwPos == end {
			finalPaths = finalPaths.Union(&path)
		}
		if state.cost == finalCost {
			continue
		}

		fwVal := arr[fwPos.y][fwPos.x]

		if fwVal != "#" {
			fwNode := Node{fwPos, dirIx}
			exState, ok := visited[fwNode]
			if !ok {
				newPathSet := path.GetCopy()
				newPathSet.Add(fwPos)
				newState := State{node: fwNode, pathSet: newPathSet, cost: state.cost + 1}
				visited[fwNode] = &newState
				heap.Push(&pq, &newState)
			} else {
				if state.cost+1 < exState.cost {
					newPathSet := path.GetCopy()
					fmt.Println("Existing Path (Cost ", exState.cost, "):")
					printPath(arr, exState.pathSet.cords)
					fmt.Println("Curr Path (Cost ", state.cost, "):")
					printPath(arr, path.cords)
					newPathSet.Add(fwPos)
					fmt.Println("New Path (Cost ", state.cost+1, "):")
					printPath(arr, newPathSet.cords)
					pq.update(exState, fwNode, newPathSet, state.cost+1)
				} else if state.cost+1 == exState.cost {
					newPathSet := path.Union(&exState.pathSet)
					pq.update(exState, fwNode, newPathSet, state.cost+1)
				}
			}
		}

		for j := -1; j <= 1; j += 2 {
			newDir := (dirIx + 4 + j) % 4
			newNode := Node{nodePos, newDir}
			exState, ok := visited[newNode]
			if !ok {
				newState := State{node: newNode, pathSet: path, cost: state.cost + 1000}
				visited[newNode] = &newState
				heap.Push(&pq, &newState)
			} else {
				if state.cost+1000 < exState.cost {
					pq.update(exState, newNode, state.pathSet, state.cost+1000)
				} else if state.cost+1000 == exState.cost {
					newPathSet := path.Union(&exState.pathSet)
					pq.update(exState, newNode, newPathSet, exState.cost)
				}
			}
		}

	}

	printPath(arr, finalPaths.cords)

	return finalPaths.Len()
}
