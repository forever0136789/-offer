# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        l=[]
        queue=[root]
        while queue:
            t=queue.pop(0)
            l.append(t.val)
            if t.left:
                queue.append(t.left)
            if t.right:
                queue.append(t.right)
        return l
