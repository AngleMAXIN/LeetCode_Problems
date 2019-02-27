package main

import "fmt"

func searchMatrix(matrix [][]int, target int) bool {
	m := len(matrix)
	if m == 0 {
		return false
	}
	n := len(matrix[0])
	if n == 0 {
		return false
	}

	h, l := m-1, 0
	for h >= 0 && l < n {
		if matrix[h][l] == target {
			return true
		} else if matrix[h][l] > target {
			h--
		} else {
			l++
		}
	}
	return false

}

func main() {
	martrix := [][]int{{-5}}
	b := searchMatrix(martrix, -5)
	fmt.Println(b)
}
