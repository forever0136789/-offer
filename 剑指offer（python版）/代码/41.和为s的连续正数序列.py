# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        a=[]
        for i in range(1,tsum):
            b=[]
            sum=i
            b.append(i)
            while sum<tsum:
                i+=1
                sum+=i
                b.append(i)
            if sum==tsum:
                a.append(b)
        return a
