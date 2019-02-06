# problem：

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]
# 

class Solution:
    def twoSum(self, nums, target):
        if len(nums) < 1:
            return False

        numdict = {}

        for i,v in enumerate(nums):
            if v in numdict:
                return [numdict[v], i]
            else:
                numdict[target - v] = i

# 思路：
# 	首先判断列表是否为空，
# 	然后首先创建一个字典，目的是存储和target相差nums[i]
# 	这么大的值（value）和nums[i]的下标i，一旦在后续的列表
# 	中找到与value相同的值，就返回字典中以value为键的值和此时的“i”值
