# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        #形成数列为1,2,3，...(代码与8题相同)
        if number==0:
            return 0
        a,b=1,1
        for i in range(number):
            a,b=b,a+b
        return a
