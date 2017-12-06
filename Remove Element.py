#/usr/bin/env python
# -*- python: utf-8 -*-

# problem:
#     Given nums = [3,2,2,3], val = 3,
#     Your function should return length = 2, with the first two elements of nums being 2.


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        while i < len(nums):   #循环条件是i始终都在nums的长度内
            if nums[i] == val:
                del nums[i]    #del掉一个元素后，nums的长度就会减一
            else:
                i = i + 1
        return len(nums)



# 思路:
#     首先判断列表是否为空，如果是，则返回0，
#     如果不是，从零开始以此遍历列表的元素，
#     遇到与val相等的值，就把它del掉，注意，此时
#     的i不能加1，否则会错过前面的元素，应该是如果没
#     有遇到与val相等的值再加1
