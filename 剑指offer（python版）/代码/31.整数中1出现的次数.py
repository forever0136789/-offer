# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res=0
        base=1
        tmp=n
        while tmp:
            weight=tmp%10
            tmp/=10
            res+=base*tmp
            if weight==1:
                res+=1+n%base
            if weight>1:
                res+=base
            base*=10
        return res
