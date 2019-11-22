# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# pre = {1,2,4,7,3,5,6,8}
# tin = {4,7,2,1,5,3,8,6}
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not any(pre, tin):
            return None

        root = pre[0]
        root_index = tin.index(root)

        NewNode = TreeNode(root.val)

        right_tin = tin[:root_index]
        left_tin = tin[root_index+1:]

        right_pre = pre[1:root_index+1]
        left_pre = pre[root_index+1:]

        right = self.reConstructBinaryTree(right_pre,right_tin)
        left = self.reConstructBinaryTree(left_pre,left_tin)
        if right:
            NewNode.right = right
        if left:
            NewNode.left = left
        return NewNode


