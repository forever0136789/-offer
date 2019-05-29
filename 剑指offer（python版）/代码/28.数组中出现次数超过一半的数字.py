# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        d={}
        for i in numbers:
            d[i]=d.get(i,0)+1
        for key,value in d.items():
            if value>len(numbers)/2:
                return key
        return 0
