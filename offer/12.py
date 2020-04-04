#coding:utf-8

'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

思路：
两个排序的链表进行合并，跟链表的插入类似，只需要比较两个链表的大小，将小的优先插入，
而后将长链表拼接到新的链表的后边即可

'''

class ListNode:
    def __init__(self,v):
        self.val=v
        self.next=None


class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1 and not pHead2:
            return
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        res=cur=ListNode(0)

        while phead1 and pHead2:
            if phead1.val<=pHead2.val:
                cur.next=phead1
                phead1=phead1.next
            else:
                cur.next=phead2.next
                phead2=phead2.next
            cur=cur.next
        if phead1:
            cur.next=phead1
        else:
            cur.next=phead2
        return res.next












if __name__ == '__main__':

    arr1=[1,3,5,7,8,9]
    arr2=[2,4,6]
    phead1=cur1=ListNode(arr1[0])
    phead2=cur2=ListNode(arr2[0])

    for n in arr1[1:]:
        cur1.next=ListNode(n)
        cur1=cur1.next
    for n in arr2[1:]:
        cur2.next=ListNode(n)
        cur2=cur2.next
    # while phead1:
    #     print(phead1.val)
    #     phead1=phead1.next

    res=cur=ListNode(0)
    while phead1 and phead2:
        if phead1.val<=phead2.val:
            cur.next=phead1
            phead1=phead1.next
        else:
            cur.next=phead2
            phead2=phead2.next
        cur=cur.next

    if phead1:
        cur.next=phead1
    else:
        cur.next = phead2

    print('res----')
    while res:
        print(res.val)
        res=res.next







