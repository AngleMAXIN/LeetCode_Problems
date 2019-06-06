class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m,len(nums1)):
        	nums1[i] = nums2[j]
        	j = j + 1 
        # nums1.extend(nums2)
        nums1.sort()

if __name__ == '__main__':
	nums1 = [1,2,3,0,0,0]
	nums2 = [2,5,6]      
	s = Solution()
	s.merge(nums1,3,nums2,3) 
	print(nums1)