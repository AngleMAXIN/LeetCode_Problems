package main

import "fmt"

/*
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

你可以假设 nums1 和 nums2 不同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5

思路：1.计算出中位数的下标，如果是数组合并后长度是偶数，中位数就要取mid 和mid-1；如果是奇数，中位数就是mid
	 2.然后将两个数组合并
	 3.判断num长度，最后取出数据，计算
*/
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	l1, i := len(nums1), 0
	l2, j := len(nums2), 0
	l3 := l1 + l2
	num := make([]int, 0)
	mid_num := l3 / 2
	for i < l1 && j < l2 {
		if nums1[i] < nums2[j] {
			num = append(num, nums1[i])
			i++
		} else {
			num = append(num, nums2[j])
			j++
		}
	}
	if j == l2 {
		num = append(num, nums1[i:]...)
	} else {
		num = append(num, nums2[j:]...)
	}
	if l3%2 != 0 {
		return float64(num[mid_num])
	} else {
		return (float64(num[mid_num]) + float64(num[mid_num-1])) / 2

	}
	return 0
}

func main() {

	num1 := []int{1, 3, 7}
	num2 := []int{3, 4, 9}

	n := findMedianSortedArrays(num1, num2)
	fmt.Println(n)
}
