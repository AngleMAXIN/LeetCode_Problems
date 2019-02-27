class Solution:
    def majorityElement(self, nums):
       """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = int(len(nums)/2)
        return nums[n]

    def majorityElement(self, nums):

    	  """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] +=1
        return max(dict1,key=dict1.get)

if __name__ == '__main__':
	l = [2,2,1,1,1,2,2]
	s = Solution()
	print(s.majorityElement(l))