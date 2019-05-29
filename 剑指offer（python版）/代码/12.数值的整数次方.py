# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        s=1
        for i in range(abs(exponent)):
            s*=base
        if exponent<0:
            return 1/s
        else:
            return s
