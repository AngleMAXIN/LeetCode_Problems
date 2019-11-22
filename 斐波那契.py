# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39

# -*- coding:utf-8 -*-
class Solution:
    _map = dict()
    def Fibonacci(self, n):
        # write code here
        if n in self._map:
            return self._map[n]

        if n <1:
            return 0
        elif n == 1 or n == 2:
            return 1
            
        v = self.Fibonacci(n-1)+self.Fibonacci(n-2)
        self._map[n] = v
        return v

s = Solution()
n = 39
r = s.Fibonacci(n)
print(r)


