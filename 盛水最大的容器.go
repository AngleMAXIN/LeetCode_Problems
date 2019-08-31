package main

import "fmt"

// 双指针解法
func maxArea(nums []int) int {

	var (
		r              = len(nums) - 1
		l              = 0
		min, max, curr int
	)

	for r >= l {
		if nums[r] < nums[l] {
			min = nums[r]
			r--
		} else {
			min = nums[l]
			l++
		}

		if curr = (r - l + 1) * min; curr > max {
			max = curr
		}

	}

	return max
}

// 暴力解法
// func maxArea(height []int) int {

// 	l := len(height)
// 	if l == 2 {
// 		if height[0] > height[1] {
// 			return height[0]
// 		}
// 		return height[1]
// 	}
// 	var (
// 		i, j          int
// 		Max, currArea int
// 	)

// 	for i = 0; i < l-1; i++ {
// 		// currArea = 0
// 		for j = i + 1; j < l; j++ {
// 			if currArea = (j - i) * currRange(height[j], height[i]); currArea > Max {
// 				Max = currArea
// 			}
// 			// fmt.Println("----", i, j, height[j], currArea)
// 		}
// 	}
// 	return Max
// }
// func currRange(a, b int) (c int) {
// 	if a <= b {
// 		c = a
// 	} else {
// 		c = b
// 	}
// 	return
// }

func main() {
	input := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	r := maxArea(input)
	fmt.Println(r)
}
