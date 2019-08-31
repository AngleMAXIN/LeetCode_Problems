package main

import "fmt"

func StrToNum(s string) int {
	l := len(s)
	if l < 1 {
		return 0
	}
	var (
		flag = 1
		// mult = 1

		start int
		Sum   int
		// temp  int
	)
	for index := 0; index < l; index++ {
		if s[index] == ' ' {
			fmt.Printf("%q\n", s[index])
			start++
		}
	}
	fmt.Println(start)

	if s[start] == '-' || s[start] == '+' {
		if s[start] == '-' {
			flag = -1
		}
		start += 1
	}
	fmt.Println(start)
	for i := start; i < l; i++ {
		if s[i] <= '9' && s[i] >= '0' {
			fmt.Println(string(s[i]), Sum)

			Sum += Sum*10 + int((s[i] - '0'))
		} else if s[i] == ' ' {
			break
		} else {
			return 0
		}
	}

	return Sum * flag
}

func main() {
	S := "4193 with words"
	r := StrToNum(S)
	fmt.Println(r)
}
