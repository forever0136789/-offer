# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        b=A[:]
        for i in range(len(b)):
            ji=1
            for j in range(len(A)):
                if j!=i:
                    ji*=A[j]
            b[i]=ji
        return b
