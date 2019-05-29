# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if abs(self.TreeDepth(pRoot.left)-self.TreeDepth(pRoot.right))>1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
        
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot:
            l=self.TreeDepth(pRoot.left)
            r=self.TreeDepth(pRoot.right)
            return max(l,r)+1
        return 0
