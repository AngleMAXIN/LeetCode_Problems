# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 上述算法可以优化为只使用一次遍历。我们可以使用两个指针而不是一个指针。第一个指针从列表的开头向前移动 n+1n+1 步，
# 而第二个指针将从列表的开头出发。现在，这两个指针被 nn 个结点分开。
# 我们通过同时移动两个指针向前来保持这个恒定的间隔，直到第一个指针到达最后一个结点。
# 此时第二个指针将指向从最后一个结点数起的第 nn 个结点。我们重新链接第二个指针所引用的结点的 next 指针指向该结点的下下个结点。
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head
        pre = end = res
        for i in range(n+1):
            pre = pre.next
        while pre:
            pre = pre.next
            end = end.next
        end.next = end.next.next
        return res.next

# a1 = ListNode(1)
# a2 = ListNode(2)
# a3 = ListNode(3)
# a4 = ListNode(4)
# a5 = ListNode(5)
#
# a1.next = a2
# a2.next = a3
# a3.next = a4
# a4.next = a5

a1 = ListNode(1)

s = Solution()
head = s.removeNthFromEnd(a1, 1)
while head:
    print(" ", head.val)
    head = head.next
# p = a1
# while p:
# 	print(p.val)
# 	p = p.next
