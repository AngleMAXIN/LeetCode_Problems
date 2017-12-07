
# problem:
#         Input: [1,3,5,6], 5
# Output: 2
# Example 2:

# Input: [1,3,5,6], 2
# Output: 1
# Example 3:

# Input: [1,3,5,6], 7
# Output: 4
# Example 1:

# Input: [1,3,5,6], 0
# Output: 0

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: return 0
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
                return len(nums)


# 思路： 首先判断列表是否为空，如果是那么target就是nums[0],
#     其次，分为两个情况，第一种，判断tatget在不在nums中，若在，找到并返回。
#     第二种，没有找到，因为是有序无重复列表，判断大于它的数的位置，就是他要放入的位置
#     ，如果没有，就说明target是最大的，则返回列表的长度即可