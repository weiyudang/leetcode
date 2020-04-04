#coding:utf-8

'''
输入一个链表，反转链表后，输出新链表的表头。
思路：
需要中间遍历保存当前节点的next  防止链表的中断
临界条件：

'''


class ListNode(object):
    def __init__(self,v):
        self.val=v
        self.next=None


class Solution:
    def ReverseList(self,pHead):
        if not pHead:
            return


        pre=None
        next=None
        while pHead:
            next=pHead.next
            pHead.next=pre
            pre=pHead
            pHead=next
        return pre



if __name__ == '__main__':

    arr=[1,2,3,4,5]
    phead=cur1=ListNode(0)
    for n in arr:
        cur1.next=ListNode(n)
        cur1=cur1.next

    pre=None
    next=None
    while phead:
        next=phead.next
        phead.next=pre
        pre=phead
        phead=next

    while pre:
        print(pre.val)
        pre=pre.next
