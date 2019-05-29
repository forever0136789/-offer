# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.isSubtree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
    def isSubtree(self,A,B):
        if not B:
            return True
        if not A or A.val!=B.val:
            return False
        return self.isSubtree(A.left,B.left) and self.isSubtree(A.right,B.right)
