package main

import "fmt"

func isPalindrome(x int) bool {
	if x < 0 || (x%10 == 0 && x != 0) {
		return false
	}
	var p int
	for p < x {
		p = p*10 + x%10
		x /= 10
	}

	return x == p || x == p/10
}

func main() {
	var c int = 0
	fmt.Println(isPalindrome(c))
}
