
# problem：
# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 
# 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        end = start = 0
        chardict = {}
        for i , c in enumerate(s):         #i代表列表的下标，c代表i下标所代表的值
            if c in chardict and start <= chardict[c]:
                start = chardict[c] + 1
                print("start:",start)
            else:
                end = max(end,i-start+1)
                print("end:",end,i,start,i-start+1)
            chardict[c] = i
            
		return end,chardict

# 思路：
	# 它的目的是求出字符串中最长的子字符串，且不包含重复的字符，
	# 首先遍历整的字符串，在这里我们用到了enumerat函数，
	# start代表查找字符串的起始位置，一旦遇到与前面重复的字符，
	# 就从之前第一个此字符的下一个位置开始计算子字符串的长度，并与之前的长度相比较
	
	
