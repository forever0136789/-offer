# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n==0:
            return -1
        res=range(n)
        #下标
        i=0
        while len(res)>1:
            i=(i+m-1)%len(res)
            res.pop(i)
        return res[0]
