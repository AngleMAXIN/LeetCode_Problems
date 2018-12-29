package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}
/*
	给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

思路：结果存入新的链表，遍历两个链表，直到所有链表遍历到空，sum用于存储和包括上一位的进位，存入新节点时还要在取余10
，carry用于存储进位值，遍历完后，判断是否最还有进位。
*/
func addTwoNumbers(node1 *ListNode, node2 *ListNode) *ListNode {
	curhead, cur1, cur2 := &ListNode{}, node1, node2
	cur := curhead
    sum, carry := 0,0
	for cur1 != nil || cur2 != nil {
        sum = carry
		if cur1 != nil {
			sum += cur1.Val
		}
		if cur2 != nil {
			sum += cur2.Val
		}
		carry = sum / 10
		cur.Next = &ListNode{Val: sum % 10}
		cur = cur.Next
		if cur1 != nil {
			cur1 = cur1.Next
		}
		if cur2 != nil {
			cur2 = cur2.Next
		}
	}
	if carry > 0 {
		cur.Next = &ListNode{Val: carry}
	}
	return curhead.Next
}
func main() {
	/*var anode1 = ListNode{Val: 2}
	var anode2 = ListNode{Val: 4}
	// var anode3 = ListNode{Val:3}
	var bnode1 = ListNode{Val: 0}
	// var bnode2 = ListNode{Val:6}
	// var bnode3 = ListNode{Val:4}
	anode1.Next = &anode2
	// anode2.Next = &anode3
	// bnode1.Next = &bnode2
	// bnode2.Next = &bnode3*/
	var anode1 = ListNode{Val: 5}
	var bnode1 = ListNode{Val: 5}
	cnode := addTwoNumbers(&anode1, &bnode1)

	for cnode != nil {
		fmt.Println(cnode.Val)
		cnode = cnode.Next
	}
}
