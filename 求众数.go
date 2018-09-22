package main

import (
	"fmt"
)

/*给定大小为n的数组，找到多数元素。多数元素是出现次数多 的元素⌊ n/2 ⌋。

您可以假设该数组非空，并且多数元素始终存在于数组中*/
xfunc majorityElement(nums []int) int {
	var count, value int

	for i := range nums {
		if count == 0 {
			value = nums[i]
			fmt.Println("value = ", value)
		}
		if value == nums[i] {
			count++
		} else {
			count--
		}
		fmt.Println("  count = ", count)
	}

	return value
}

func main() {
	nums := []int{2, 2, 1, 1, 5, 1, 2, 2, 1, 1}
	t := majorityElement(nums)
	fmt.Println(t)
}
