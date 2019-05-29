# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.comRoot(pRoot.left,pRoot.right)
    
    def comRoot(self,Left,Right):
        if not Left:
            return (not Right)
        if not Right:
            return False
        if Left.val!=Right.val:
            return False
        return self.comRoot(Left.left,Right.right) and self.comRoot(Left.right,Right.left)
