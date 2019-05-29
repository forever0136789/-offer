# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        number=map(str,numbers)
        number.sort(lambda x,y:cmp(x+y,y+x))
        return ''.join(number)
