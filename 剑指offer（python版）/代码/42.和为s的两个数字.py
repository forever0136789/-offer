# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        n=len(array)
        l=[]
        for i in range(0,n-1):
            for j in range(1,n):
                if array[i]+array[j]==tsum:
                    l.append([array[i],array[j]])
                    break
        if len(l)==0:
            return []
        else:
            return l[0]
