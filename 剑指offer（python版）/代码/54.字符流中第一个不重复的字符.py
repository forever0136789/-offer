# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s=''
        self.d={}
        
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.d[i]==1:
                return i
        return '#'
        
    def Insert(self, char):
        # write code here
        self.s+=char
        self.d[char]=self.d.get(char,0)+1
