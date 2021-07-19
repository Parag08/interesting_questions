package main

import "fmt"

type Queue struct {
	IntArr    []int
	StrintArr []string
	CharArr   []rune
}

func (q *Queue) EnqueueInt(i int) {
	q.IntArr = append(q.IntArr, i)
}

func (q *Queue) DequeueInt() (i int) {
	i = q.IntArr[0]
	q.IntArr = q.IntArr[1:]
	return i
}

type Stack struct {
	IntArr    []int
	StrintArr []string
	CharArr   []rune
}

func (s *Stack) Push(i int) {
	s.IntArr = append(s.IntArr, i)
}

func (s *Stack) Pop() (i int) {
	i = s.IntArr[len(s.IntArr)]
	s.IntArr = s.IntArr[:len(s.IntArr)-1]
	return i
}

func main() {
	var q Queue
	q.EnqueueInt(0)
	q.EnqueueInt(1)
	fmt.Println(q.DequeueInt())
	fmt.Println(q.DequeueInt())
}
