# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        #原链表临时指针
        head=pHead
        #新链表头
        phead=None
        #新链表临时指针
        tmp=None
        old_new_dic={}
        random_dic={}
        while head:
            node=RandomListNode(head.label)
            node.random=head.random
            old_new_dic[id(head)]=id(node)
            random_dic[id(node)]=node
            head=head.next
            
            if phead:
                tmp.next=node
                tmp=tmp.next
            else:
                phead=node
                tmp=node
        tmp=phead
        while tmp:
            if tmp.random!=None:
                tmp.random=random_dic[old_new_dic[id(tmp.random)]]
            tmp=tmp.next
        return phead
