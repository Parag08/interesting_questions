package main

import "fmt"

func gridTraveler(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])
	var table = make([][]int, m)
	for i := 0; i < m; i++ {
		table[i] = make([]int, n)
	}
	fmt.Println(table)
	return 0
}

func main() {
	gridTraveler([][]int{
		{0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0}})
}
