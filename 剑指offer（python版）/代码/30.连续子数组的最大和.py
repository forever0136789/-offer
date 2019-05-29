# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        l=[]
        this_sum=0
        for i in array:
            this_sum+=i
            l.append(this_sum)
            if this_sum<0:
                this_sum=0
        return max(l)
