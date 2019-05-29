# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data=[]
    
    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()
        
    def GetMedian(self,data):
        # write code here
        n=len(self.data)
        if n%2==0:
            return (self.data[n/2]+self.data[n/2-1])/2.0
        else:
            return self.data[n/2]
