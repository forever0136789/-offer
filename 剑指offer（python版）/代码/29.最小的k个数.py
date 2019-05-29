# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput)<k:
            return []
        tinput.sort()
        return tinput[:k]
