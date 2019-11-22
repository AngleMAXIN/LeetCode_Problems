# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        sl = len(s)
        space_num = 0

        for i in s:
            if i == " ":
                space_num += 1

        total_len = sl+space_num * 3
        final_str = ""
        for i in range(sl):
            if s[i] == " ":
                final_str += "%20"
            else:
                final_str += s[i]
        return final_str


Str = "We Are Happy"
s = Solution()
res = s.replaceSpace(Str)
print(res)