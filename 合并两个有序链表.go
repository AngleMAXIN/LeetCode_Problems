package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	//var ptr ListNode
	var head  = &ListNode{}
	var ptr = head
	for  l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
			head.Next = l1
			l1 = l1.Next
			head = head.Next
		} else {
			head.Next = l2
			l2 = l2.Next
			head = head.Next
		}

	}

	if l1 != nil {
		head.Next = l1
	}
	if l2 != nil {
		head.Next = l2
	}
	return ptr.Next
}

func main() {
	var a1, a2, a3 ListNode
	var b1, b2, b3 ListNode
	a1.Val = 1
	a1.Next = &a2
	a2.Val = 2
	a2.Next = &a3
	a3.Val = 4
	a3.Next = nil

	b1.Val = 1
	b1.Next = &a2
	b2.Val = 3
	b2.Next = &a3
	b3.Val = 4
	b3.Next =  nil
	p := mergeTwoLists(&a1,&b1)
	fmt.Println(p)

}
