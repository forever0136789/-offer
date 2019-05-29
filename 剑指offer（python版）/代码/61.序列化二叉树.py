# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    flag=-1
    def Serialize(self, root):
        # write code here
        s=''
        s=self.recursionSerialize(root,s)
        return s
    
    def recursionSerialize(self,root,s):
        if not root:
            s='$,'
            return s
        s=str(root.val)+','
        left=self.recursionSerialize(root.left,s)
        right=self.recursionSerialize(root.right,s)
        s=s+left+right
        return s
        
    def Deserialize(self, s):
        # write code here
        l=s.split(',')
        self.flag+=1
        root=None
        if l[self.flag]!='$':
            root=TreeNode(int(l[self.flag]))
            root.left=self.Deserialize(s)
            root.right=self.Deserialize(s)
        return root
