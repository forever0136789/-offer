# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        t1=pHead1
        t2=pHead2
        #对象的成员变量任意给值
        head=ListNode(-1)
        t=head
        while t1 and t2:
            if t1.val<t2.val:
                t.next=t1
                t1=t1.next
            else:
                t.next=t2
                t2=t2.next
            t=t.next
        t.next=t1 or t2
        return head.next
