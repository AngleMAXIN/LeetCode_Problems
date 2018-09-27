/*
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
       /
      8
返回它的最大深度 4 。

思路: 迭代
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

package main

import (
	"fmt"
)

type ListNode struct {
	Val   int
	Left  *ListNode
	Right *ListNode
}

func maxDepth(root *ListNode) int {
	if root == nil {
		return 0
	}
	fmt.Println("in root: ", *root)
	Left := maxDepth(root.Left)
	Right := maxDepth(root.Right)
	fmt.Println("out root: ", *root, "left: ", Left, "right: ", Right)
	if Left < Right {
		fmt.Println("right--- ")
		return Right + 1
	} else if Left > Right {
		fmt.Println("left ---")
		return Left + 1
	} else {
		fmt.Printf("ok-------\n")
		return Left + 1
	}

}

func main() {
	// var a1, list[i], a2, a4, a5, a6 ListNode
	var alist = [6]ListNode{}
	var li = []int{3, 9, 20, 15, 7, 8}
	for i := 0; i < 6; i++ {
		alist[i].Val = li[i]
		fmt.Println(alist[i].Val)
	}
	alist[0].Left = &alist[1]
	alist[0].Right = &alist[2]
	alist[2].Left = &alist[3]
	alist[2].Right = &alist[4]
	alist[4].Left = &alist[5]

	re := maxDepth(&alist[0])
	fmt.Println(re)
}
