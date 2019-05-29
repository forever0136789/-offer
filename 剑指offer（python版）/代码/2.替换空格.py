# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s1=''
        for i in s:
            if i==' ':
                s1+='%20'
            else:
                s1+=i
        return s1
