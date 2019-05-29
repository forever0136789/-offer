# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size<=0:
            return []
        result=[]
        for i in range(len(num)-size+1):
            result.append(max(num[i:i+size]))
        return result
