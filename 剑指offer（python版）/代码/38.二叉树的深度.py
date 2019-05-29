# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot:
            l=self.TreeDepth(pRoot.left)
            r=self.TreeDepth(pRoot.right)
            return max(l,r)+1
        return 0
