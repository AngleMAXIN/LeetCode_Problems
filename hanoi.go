package main

import (
	"fmt"
)

func hanoi(n int, a, b, c byte) {
	if n == 1 {
		fmt.Printf("%c-->%c\n", a, c)
	} else {
		hanoi(n-1, a, c, b)           // move a to b by c
		fmt.Printf("%c-->%c\n", a, c) // move last one to c from a
		hanoi(n-1, b, a, c)           // move b to c by a
	}
}

func main() {
	z
	hanoi(5, 'a', 'b', 'c')
}
