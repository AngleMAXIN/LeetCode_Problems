# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        stack = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        stack.reverse()
        return stack

a = ListNode(3)
b = ListNode(2)
c = ListNode(1)

a.next = b
b.next = c

s = Solution()
res = s.printListFromTailToHead(a)
print(res)