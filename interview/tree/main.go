package main

import "fmt"

type Tree struct {
	Val   int
	Right *Tree
	Left  *Tree
}

func main() {
	input := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	root := &Tree{
		Val: input[0],
	}
	trav := root
	for i := 1; i < len(input); i++ {
		if i%2 == 1 {
			trav.Right = &Tree{Val: input[i]}
		} else {
			trav.Left = &Tree{Val: input[i]}
			trav = trav.Right
		}
	}
	// LDR(root)
	PopulateTreeMap(root)
	fmt.Println(treeMap)
}

func LDR(root *Tree) {
	if root == nil {
		return
	}
	LDR(root.Left)
	fmt.Println(root.Val)
	LDR(root.Right)
}

type Child struct {
	Left  int
	Right int
}

var treeMap = make(map[int]Child)

func PopulateTreeMap(root *Tree) {
	if root == nil {
		return
	}
	var (
		ch    Child
		left  = false
		right = false
	)
	if root.Left != nil {
		ch.Left = root.Left.Val
		left = true
	}
	if root.Right != nil {
		ch.Right = root.Right.Val
		right = true
	}
	if right || left {
		treeMap[root.Val] = ch
	}
	PopulateTreeMap(root.Left)
	PopulateTreeMap(root.Right)
}
