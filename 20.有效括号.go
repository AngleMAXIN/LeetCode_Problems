package main

import "fmt"

func isValid(s string) bool {
	length := len(s)

	if length == 1 || length%2 != 0 {
		return false
	} else if length == 0 {
		return true
	}

	reStr := map[byte]byte{
		']': '[',
		')': '(',
		'}': '{',
	}

	stack := make([]byte, 0)
	for i := 0; i < length; i++ {
		if v, ok := reStr[s[i]]; ok {
			if len(stack) != 0 && stack[len(stack)-1] == v {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}

		} else {
			stack = append(stack, s[i])
		}
	}
	if len(stack) != 0 {
		return false
	}
	return true
}

func Beter_isValid(s string) bool {
	mp := map[byte]byte{')': '(', ']': '[', '}': '{'}
	st := make([]byte, len(s))
	index := 0
	for i := 0; i < len(s); i++ {
		if index == 0 || mp[s[i]] != st[index-1] {
			st[index] = s[i]
			index++
		} else {
			index--
		}
	}
	return index == 0
}

func main() {

	s := "(("
	r := isValid(s)
	fmt.Println(r)
	// for i, v := range s {
	// 	fmt.Printf("%T,%T,%v\n", i, v, i)
	// }
}
