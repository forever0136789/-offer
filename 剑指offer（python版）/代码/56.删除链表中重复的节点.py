# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        tmp=pHead.next
        if tmp.val==pHead.val:
            while tmp and tmp.val==pHead.val:
                tmp=tmp.next
            return self.deleteDuplication(tmp)
        else:
            pHead.next=self.deleteDuplication(tmp)
            return pHead