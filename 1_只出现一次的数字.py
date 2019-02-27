class Solution:
    def singleNumber(self, nums):
        count_dict = {}
        for i in nums:
            if i in count_dict:
            	# print("---")
                count_dict[i] = 2
                # print("--",i)
                continue
            count_dict[i] = 1

        # print(count_dict)
        for i in count_dict.items():
        	# print(i)
        	if i[1] == 1:
        		return i[0]
            # if count_dict[i] == 1:
                # return i
if __name__ == '__main__':
	d = [2,2,1]
	s = Solution()
	a = s.singleNumber(d)
	print(a)