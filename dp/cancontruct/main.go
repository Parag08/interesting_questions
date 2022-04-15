package main

import "fmt"

var memo = make(map[string][][]string)
var count = 0

func canConstruct(target string, array []string) [][]string {
	var ways = [][]string{}
	if target == "" {
		return [][]string{}
	}
	if val, ok := memo[target]; ok {
		return val
	}
	for _, str := range array {
		numways := [][]string{}
		if str == target {
			return [][]string{[]string{str}}
		}
		if len(str) > len(target) {
			continue
		}
		if target[:len(str)] == str {
			numways = canConstruct(target[len(str):], array)
			//fmt.Println(numways)
			for i, _ := range numways {
				numways[i] = append(numways[i], str)
			}
			//fmt.Println(numways)
		}
		ways = append(ways, numways...)
	}
	memo[target] = ways
	return ways
}

func main() {
	fmt.Println(canConstruct("abcdef", []string{"ab", "abc", "cd", "def", "abcd"}))
	//fmt.Println(canConstruct("skateboard", []string{"bo", "rd", "ate", "t", "ska", "sk", "boar"}))
	//fmt.Println(canConstruct("eeeeeeeeeeeeeeeeeeeeef", []string{"e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeeee"}))
	fmt.Println(canConstruct("purple", []string{"purp", "p", "ur", "le", "purpl"}))
}
