# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        head1=pHead1
        head2=pHead2
        list1=[]
        while head1:
            list1.append(head1.val)
            head1=head1.next
        while head2:
            if head2.val in list1:
                return head2
            else:
                head2=head2.next
