/*
编写一个函数，其作用是将输入的字符串反转过来。

示例 1:

输入: "hello"
输出: "olleh"
示例 2:

输入: "A man, a plan, a canal: Panama"
输出: "amanaP :lanac a ,nalp a ,nam A"
*/
package main

import (
	"fmt"
)

func main() {

	num := make([]byte, 0)
	num = []byte{6, 7, 8, '8'}
	// str := []byte(num)
	fmt.Printf("%T\t%T", num[0], num[3])
}

/*
func reverseString(s string) string {
	strl := make([]byte, 0)
	l := len(s) - 1
	for i := l; i >= 0; i-- {
		strl = append(strl, s[i])
	}
	return string(strl)
}
*/
