# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        
        root=sequence[-1]
        i=0
        while sequence[i]<root:
            i+=1
        k=i
        for i in range(k,len(sequence)-1):
            if sequence[i]<root:
                return False
        left=sequence[:k]
        right=sequence[k:len(sequence)-1]
        
        bool_left=True
        bool_right=True
        if len(left):
            bool_left=self.VerifySquenceOfBST(left)
        if len(right):
            bool_right=self.VerifySquenceOfBST(right)
        return bool_left and bool_right
