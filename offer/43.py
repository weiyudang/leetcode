#coding:utf-8
'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
链表中的环：
可以使用快慢指针的方式进行
快指针每次走两步
慢指针每次走一步
如果直至相等，然后快指针再从头走，直至相遇，则就是

'''

class ListNode:
    def __init__(self,v):
        self.val=v
        self.left=None
        self.right=None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        fast=pHead.next.next
        low=pHead.next
        while fast!=low:
            if fast.next.next is None and low.next is None:
                return  None
            fast=fast.next.next
            low=low.next
        fast=pHead
        while fast!=low:
            low=low.next
            fast=fast.next
        return  fast







if __name__ == '__main__':
    array=[1,2,3,4]
    commom=[10,11,12]
