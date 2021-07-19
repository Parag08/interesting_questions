package main

import "fmt"

type Nodes struct {
	Val  int
	Next *Nodes
}

func main() {
	input := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	root := &Nodes{
		Val: input[0],
	}
	last := root
	for i := 1; i < len(input); i++ {
		temp := &Nodes{
			Val: input[i],
		}
		last.Next = temp
		last = last.Next
	}
	//insert(root, 1, input)
	// printElem(root)
	// fmt.Println(findlen(root))
	// middle := findMiddle(root)
	// fmt.Println(middle.Val)
	makeCircular(root, 4)
	fmt.Println(findCircular(root))
}

func makeCircular(root *Nodes, i int) error {
	if root == nil || root.Next == nil {
		return fmt.Errorf("cant make this linked list circular")
	}
	var (
		addrI *Nodes
		j     = 0
	)
	for root.Next != nil {
		if j == i {
			addrI = root
		}
		j = j + 1
		root = root.Next
	}
	if addrI == nil {
		return fmt.Errorf("cant find the i th node")
	}
	root.Next = addrI
	return nil
}

// Print all elem in list
func printElem(root *Nodes) {
	if root == nil {
		return
	} else {
		fmt.Println(root.Val)
		next := root.Next
		printElem(next)
	}
}

func findlen(root *Nodes) int {
	if root == nil {
		return 0
	} else {
		return findlen(root.Next) + 1
	}
}

// insert elem in a recuressive manner
func insert(root *Nodes, i int, input []int) {
	if i < len(input) {
		temp := &Nodes{
			Val: input[i],
		}
		root.Next = temp
		insert(temp, i+1, input)
	} else {
		return
	}
}

// find middle elem
func findMiddle(root *Nodes) *Nodes {
	twoXpointer := root
	oneXpointer := root
	if root.Next == nil {
		return root
	}
	for {
		if twoXpointer.Next != nil && twoXpointer.Next.Next != nil {
			twoXpointer = twoXpointer.Next.Next
		} else {
			break
		}
		oneXpointer = oneXpointer.Next
	}
	return oneXpointer
}

// find circular
func findCircular(root *Nodes) bool {
	isCircular := false
	if root == nil {
		return isCircular
	}
	twoXpointer := root
	oneXpointer := root
	if root.Next == nil {
		return isCircular
	}
	for {
		if twoXpointer.Next != nil && twoXpointer.Next.Next != nil {
			twoXpointer = twoXpointer.Next.Next
		} else {
			break
		}
		oneXpointer = oneXpointer.Next
		if oneXpointer == twoXpointer {
			isCircular = true
			break
		}
	}
	return isCircular
}
