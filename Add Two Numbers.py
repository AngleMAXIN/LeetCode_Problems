

# problem：
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None    #指向下一个类的指针

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        res = []
        
        while l1 or l2 or carry:

        	a = b = 0

        	if l1:
        		a = l1.val
        		l1 = l1.next
        	if l1:
        		b = l2.val
        		l2 = l2.next

        	temp = a + b + carry
        	res.append(temp%10)
        	carry = temp // 10

        return res

# 思路：
# 	你可以把ListNode当做一个带有指针的结构体，
# 	首先carry是尾巴，目的是如果之前两个数的和
# 	大于10，那么对其整除（注意结果是整数），其整
# 	除后的结果便赋值给carry，并将carry加在之后的
# 	a、b之和的后面，在将temp添加进数组时，应是取余后的结果