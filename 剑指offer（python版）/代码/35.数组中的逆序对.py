# -*- coding:utf-8 -*-
p=0
class Solution:
    def InversePairs(self, data):
        # write code here
        self.merge_sort(data)
        return p%1000000007
    
    def merge_sort(self,data):
        if len(data)<=1:
            return data
        global p
        mid=len(data)//2
        left=self.merge_sort(data[:mid])
        right=self.merge_sort(data[mid:])
        i=0
        j=0
        result=[]
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
                p+=len(left)-i
        result.extend(left[i:])
        result.extend(right[j:])
        return result
