# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0:
            return 0
        min=rotateArray[0]
        for i in range(1,len(rotateArray)):
            if rotateArray[i]<min:
                min=rotateArray[i]
        return min
