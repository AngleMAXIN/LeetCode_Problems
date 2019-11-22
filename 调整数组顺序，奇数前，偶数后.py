# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, a):
        # write code here
        l = len(a)
        if l < 2:
            return a
        ou = 1
        ji = 0
        while ou < l-1:
            if a[ou] & 1 == 1 and a[ji] & 1 == 0:
                #a[ou] = a[ou] ^ a[ji]
                #a[ji] = a[ou] ^ a[ji]
                #a[ou] = a[ou] ^ a[ji]
                a[ou],a[ji] = a[ji],a[ou]
            ou += 1
            ji += 1
        return a 
        
# [1,3,5,7,2,4,6]
a = [1,2,3,4,5,6,7]
s = Solution()
r = s.reOrderArray(a)
print(r)