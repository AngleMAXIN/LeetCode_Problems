

# problem：
# 	Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.
# 

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        id = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[id]:
                id += 1                #保证第一个即下标为0时，不被覆盖
                nums[id] = nums[i]
                
        return id+1

# 思路：
	# 从列表的第二个元素开始查找，如果与前面的元素不相同，就往后依次赋值，如果相同，不表示，直到最后返回长度id+1