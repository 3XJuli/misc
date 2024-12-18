package main

import (
	"container/heap"
	"strings"
)

func part01(input string) int {

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
	pq[0] = &State{node: initNode, cost: 0, index: 0}

	visited[initNode] = pq[0]

	heap.Init(&pq)

	for pq.Len() > 0 {
		state := heap.Pop(&pq).(*State)

		node := state.node
		dirIx := node.dir
		nodePos := node.pos

		fwPos := cord{nodePos.x + directions[dirIx].x, nodePos.y + directions[dirIx].y}

		if fwPos == end {
			return state.cost + 1
		}

		fwVal := arr[fwPos.y][fwPos.x]

		if fwVal != "#" {
			fwNode := Node{fwPos, dirIx}
			exState, ok := visited[fwNode]
			if !ok {
				newState := State{node: fwNode, cost: state.cost + 1}
				visited[fwNode] = &newState
				heap.Push(&pq, &newState)
			} else {
				if state.cost+1 < exState.cost {
					pq.update(exState, fwNode, SimpleSet{}, state.cost+1)
				}
			}
		}

		for j := 1; j < 4; j++ {
			newDir := (dirIx + j) % 4
			newNode := Node{nodePos, newDir}
			exState, ok := visited[newNode]
			if !ok {
				newState := State{node: newNode, cost: state.cost + 1000}
				visited[newNode] = &newState
				heap.Push(&pq, &newState)
			} else {
				if state.cost+1000 < exState.cost {
					pq.update(exState, newNode, SimpleSet{}, state.cost+1000)
				}
			}
		}

	}

	return -1
}
