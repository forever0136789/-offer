# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        l=[]
        for i in array:
            if array.count(i)==1:
                l.append(i)
        return l
