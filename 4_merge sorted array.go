package main

import (
	"fmt"
)

func merge(nums1 []int, m int, nums2 []int, n int)  {
	i := m - 1
	j := n - 1
    k :=  m+n - 1

    for i >= 0 && j >= 0 {
    	if nums1[i] > nums2[j] {
    		nums1[k] = nums1[i]
    		i--
    	} else {
    		nums1[k] = nums2[j]
    		j--
    	}
    	k--
    }

    for j >= 0 {
    	nums1[k] = nums2[j]
    	k-- 
    	j--
    }
}

func main() {
	a := []int{1,4,17,0,0,0,0,0}
	b := []int{6,8,12,16,139}
	m,n := 3,5
	merge(a, m, b, n)
	fmt.Println(a)
}