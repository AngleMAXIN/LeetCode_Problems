# problem：
# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of
# 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring
import time
# 思路:
#     首先需要一个字典记录字符串中的字符出现的最新下标,end表示最优子串的长度,
#     start表示子串的起始位置,如果元素在字典中,既有重复元素出现,并且起始位置小于
#     该元素在字符串中的位置,就更新start为被发现重复元素位置的加一,而不是start+1,如果元素不在
#     字典中,就更新子串的长度,即i - start + 1最后无论如何都要更新元素在字符串中
#     的位置,最后的end即为结果

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        end = start = 0
        chardict = {}
        for i, c in enumerate(s):  # i代表列表的下标，c代表i下标所代表的值
            if c in chardict and start <= chardict[c]:
                start = chardict[c] + 1
                # print("start:", start)
            else:
                end = max(end, i - start + 1)
                # print("end:", end, i, start, i - start + 1)
            chardict[c] = i
        return end

#
# class Solution2:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         lenght = len(s)
#         if lenght < 1:
#             return s
#         i = j = l = le = 0
#         print(i, j, l, le, lenght)
#         while i < lenght:
#             j = i
#             while j < lenght - 1:
#                 if s[j + 1] != s[i]:
#                     j += 1
#                 else:
#                     break
#             le = j - i + 1
#             print("le == ", le)
#             if le > l:
#                 l = le
#             i += 1
#         return l


string = "s9CabcNEu8eqweeqer"
Solution1 = Solution()
# Solution2 = Solution2()

start = time.time()
t = Solution1.lengthOfLongestSubstring(string)
print("one: ", time.time() - start, t)

# start = time.time()
# t = Solution2.lengthOfLongestSubstring(string)
# print("second: ",time.time() - start,t)

# 思路：
# 它的目的是求出字符串中最长的子字符串，且不包含重复的字符，
# 首先遍历整的字符串，在这里我们用到了enumerat函数，
# start代表查找字符串的起始位置，一旦遇到与前面重复的字符，
# 就从之前第一个此字符的下一个位置开始计算子字符串的长度，并与之前的长度相比较
