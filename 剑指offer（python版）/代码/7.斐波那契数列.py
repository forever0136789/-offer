# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n==0:
            return 0
        if n==1:
            return 1
        a,b=1,1
        for i in range(n-1):
            a,b=b,a+b
        return a
