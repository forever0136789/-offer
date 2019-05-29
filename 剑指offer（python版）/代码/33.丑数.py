# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index<=0:
            return 0
        ugly_list=[1]
        index_two=0
        index_three=0
        index_five=0
        for i in range(index-1):
            new_ugly=min(ugly_list[index_two]*2,ugly_list[index_three]*3,ugly_list[index_five]*5)
            ugly_list.append(new_ugly)
            if new_ugly%2==0:
                index_two+=1
            if new_ugly%3==0:
                index_three+=1
            if new_ugly%5==0:
                index_five+=1
        return ugly_list[-1]
