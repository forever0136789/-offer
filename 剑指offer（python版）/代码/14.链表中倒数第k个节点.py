# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        l=[]
        while head:
            l.append(head)
            head=head.next
        if k<=0 or k>len(l):
            return
        return l[-k]
