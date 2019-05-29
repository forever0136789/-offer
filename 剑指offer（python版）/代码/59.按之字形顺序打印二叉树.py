# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        result=[]
        flag=False
        queue=[pRoot]
        while queue:
            n=len(queue)
            l=[]
            for i in range(n):
                cur_node=queue.pop(0)
                l.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            if flag:
                result.append(l[::-1])
            else:
                result.append(l)
            flag=not flag
        return result
