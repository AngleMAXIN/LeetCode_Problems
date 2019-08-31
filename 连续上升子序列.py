class Solution():
    def maxSeqence(self, nums):
        lenght = len(nums)
        if lenght <= 1:
            return lenght

        max = 0
        # for i in range(1, lenght):
        #     curr = 1
        i = 1
        curr = 1
        while i < lenght:
            if nums[i] > nums[i-1]:
                curr += 1
            else:
                curr = 1

            if curr > max:
                max = curr
            i += 1

        return max


nums = [1,3,5,4,7]
s = Solution()
r = s.maxSeqence(nums)
print(r)
