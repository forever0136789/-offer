# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for i in range(len(array)):
            for j in range(len(array[0])):
                if target==array[i][j]:
                    return True
                if target>array[i][j]:
                    continue
                else:
                    break
        return False
