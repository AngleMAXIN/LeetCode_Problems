
# problem:
#     For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# 思路：找了许多资料，才勉强明白了点--动态规划，做出最优的抉择，cursum可以当做当下最优的抉择，
# 如果当前的num比之前的cursum+num大，那么就抛弃它，重新从num开始，并与之前保留的最大值比较

class Solution:
    def maxSubArray(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A:
            return 0        
        curSum = maxSum = A[0]
        for num in A[1:]:           
            curSum = max(num, curSum + num)           
            maxSum = max(maxSum, curSum)
        return maxSum

 p = Project()