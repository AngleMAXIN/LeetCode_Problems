package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

/*反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

*/
func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	if head.Next == nil {
		return head
	}

	var next, pre *ListNode
	for head != nil {
		next = head.Next // next 指向当前头结点的下一个结点,保留住这个结点
		head.Next = pre  // 让其结点指向pre,一开始是nil,而后就是其头结点的上一个结点
		pre = head       // 让这个pre指针指向当前的头结点,转向,间接赋值给next
		head = next      // 再把头结点依次迭代
	}
	return pre
}

func main() {
	var head, p1, p2, p3 ListNode
	head.Val = 0
	head.Next = &p1
	p1.Val = 2
	p1.Next = &p2
	p2.Val = 3
	p2.Next = &p3
	p3.Val = 4
	p3.Next = nil

	fmt.Println(reverseList(&head))
}
