# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        a=[]
        b=[]
        for i in array:
            if i%2!=0:
                a.append(i)
            else:
                b.append(i)
        a.extend(b)
        return a
