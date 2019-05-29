# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        global result
        result=[]
        self.midnode(pRoot)
        if k<1 or k>len(result):
            return None
        return result[k-1]
    
    def midnode(self,pRoot):
        if not pRoot:
            return None
        self.midnode(pRoot.left)
        result.append(pRoot)
        self.midnode(pRoot.right)
