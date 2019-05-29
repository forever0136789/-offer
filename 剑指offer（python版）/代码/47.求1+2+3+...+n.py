# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return reduce((lambda x,y:x+y),range(1,n+1))
