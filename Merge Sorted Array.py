#/usr/bin/env python
# -*- python: utf-8 -*-

# problem:
# 给定两个排序整数数组nums1和nums2，将nums2合并为nums1作为一个排序数组。
#
# 注:
#
# 您可以假设nums1有足够的空间(大小大于或等于m + n)，以容纳来自nums2的额外元素。nums1和nums2中初始化的元素数量分别为m和n。

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

# 思路：
#     由于是排好序的数组，我们可以先从最后一个开始比较，若nums1的值val1大于等于nums2的值val2，
#     在完全排序后要放入的位置放入val1，若相反，执行类似的操作，
#     并将其下标减一。若其中nums1数组遍历结束，就将其nums2的后续元素全部放在nums1中剩余的位置
#     之所以从后面添加，是省去了从前面开始添加，要一个个往后位移的过程。
#     复杂度O(m+n)