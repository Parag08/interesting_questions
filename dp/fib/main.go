package main

import "fmt"

func fib(val int) int {
	last := 1
	lastlast := 0
	current := 0
	if val == 1 {
		return last
	}
	for i := 2; i <= val; i++ {
		//fmt.Println(lastlast, last, current)
		current = last + lastlast
		lastlast = last
		last = current
	}
	return current
}

func main() {
	fmt.Println(fib(50))
}
