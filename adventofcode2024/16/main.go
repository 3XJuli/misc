package main

import (
	"adventofcode/util"
	"container/heap"
	_ "embed"
	"flag"
	"fmt"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type cord struct {
	x, y int
}

func checkValid(checkCord cord, dims cord) bool {
	return checkCord.x >= 0 && checkCord.x < dims.x && checkCord.y >= 0 && checkCord.y < dims.y
}

var directions = [4]cord{
	{-1, 0},
	{0, -1},
	{1, 0},
	{0, 1},
}

type Node struct {
	pos cord
	dir int
}

type State struct {
	node    Node
	pathSet SimpleSet
	cost    int
	index   int
}

type PriorityQueue []*State

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].cost < pq[j].cost
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x any) {
	n := len(*pq)
	item := x.(*State)
	item.index = n
	*pq = append(*pq, item)
}
func (pq *PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil
	item.index = -1
	*pq = old[0 : n-1]
	return item
}
func (pq *PriorityQueue) update(state *State, node Node, pathSet SimpleSet, cost int) {
	state.node = node
	state.pathSet = pathSet
	state.cost = cost
	heap.Fix(pq, state.index)
}

//go:embed input
var input string

func main() {
	var part int
	flag.IntVar(&part, "part", 1, "part 1 or part 2")

	flag.Parse()

	fmt.Println("Running Part", part)

	var ans int

	if part == 1 {
		ans = part01(input)
	} else {
		ans = part02(input)
	}
	err := util.CopyToClipboard(fmt.Sprintf("%v", ans))

	check(err)

	fmt.Println("Output (copied to clipboard):", ans)
}
