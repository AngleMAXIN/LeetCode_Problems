# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def IsSubTree(self, p1, p2):
        if not p1:
            return False
        if not p2:
            return True
        if p1.val == p2.val:
            return self.IsSubTree(p1.left, p2.left) && self.IsSubTree(p1.right, p2.right)
        else:
            return False

    def HasSubtree(self, p1, p2):
        # write code here
        if not p1 or not p2:
            return False
        return self.IsSubTree(p1, p2) || self.HasSubtree(p1.left, p2) || self.HasSubtree(p1.right, p2)
