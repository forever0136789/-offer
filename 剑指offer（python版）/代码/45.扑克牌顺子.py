# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers)!=5:
            return False
        new_list=sorted([m for m in numbers if m>0])
        n=0
        for i in range(len(new_list)-1):
            if new_list[i+1]>new_list[i]:
                n+=new_list[i+1]-new_list[i]
            else:
                return False
        if n<=4:
            return True
        else:
            return False
