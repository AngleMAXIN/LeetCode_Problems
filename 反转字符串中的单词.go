/*package main

import (
	"fmt"
	"strings"
)

func reverseString(str1 string) string {
	split_str := strings.Fields(str1)
	strll := make([]string, 0)

	for _, s := range split_str {
		l := len(s) - 1
		fmt.Println("1----", s)
		var strl []byte

		for i := l; i >= 0; i-- {
			strl = append(strl, s[i])
		}
		fmt.Println("2---", string(strl))
		strll = append(strll, string(strl))
	}
	fmt.Println("00000", len(strll))
	for i, v := range strll {
		fmt.Println(i, v)
	}
	return string(strings.Join(strll, " "))
}

func main() {
	str := "Let's take LeetCode contest"
	// 	fmt.Printf("Fields are: %q\n", strings.Fields(str))
	// 	fmt.Printf("%q\n", strings.Split(str, " "))
	res := reverseString(str)
	fmt.Println("3----\n", res)
}
*/




/*给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。*/


func reverseWords(s string) string {
    l := len(s)
    if l <= 1 {
        return s
    }
    res := make([]byte, l)
    for i := 0; i < l; i++ {
        res[i] = s[i]
    }
    left, right := 0, 0
    for ; right < l; right++ {
        if res[right] != byte(' ') {continue}
        swap(res, left, right-1)
        left = right+1
    }
    swap(res, left, right-1)
    return string(res)
}

func swap(b []byte, left, right int) {
    for left < right {
        b[left], b[right] = b[right], b[left]
        left++
        right--
    }
}