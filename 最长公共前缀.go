package main

import "fmt"

/*
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
*/
func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	var (
		i, j, min int
		minLen    = len(strs[0])
	)

	for j, _ := range strs {
		if min = len(strs[j]); min < minLen {
			minLen = min
		}
	}
	for i = 0; i < minLen; i++ {
		curr := strs[0][i]
		for index, _ := range strs {
			if strs[index][i] != curr {
				goto END
			}
		}
	}
END:
	return strs[j][:i]
}

func main() {
	input := []string{"9flower", "flow", "flight"}
	r := longestCommonPrefix(input)
	fmt.Println(r)
}
