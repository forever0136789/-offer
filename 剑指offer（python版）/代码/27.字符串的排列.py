# -*- coding:utf-8 -*-
import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        return sorted(set(map(''.join,itertools.permutations(ss))))
