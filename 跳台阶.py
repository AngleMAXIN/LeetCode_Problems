# -*- coding:utf-8 -*-
# #题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）

class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number < 1:
            return 0
        if number == 1:
            return 1
        f = 1
        while number >= 2:
            f = 2 * f
            number -= 1
        return f 