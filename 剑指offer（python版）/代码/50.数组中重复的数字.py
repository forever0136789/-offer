# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        d={}
        for i in numbers:
            d[i]=d.get(i,0)+1
            if d[i]==2:
                duplication[0]=i
                return True
        return False
