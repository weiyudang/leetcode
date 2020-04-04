#coding:utf-8
'''
输入一个链表，输出该链表中倒数第k个结点。
思路：
快慢指针法 （与两分查找的双指针法不同）
1.快指针首先走k 步
2.快慢指针同时走知道快指针走到链表的尾部,则慢指针就是倒数第k个节点
特殊条件
1.链表的长度小于k


'''
class ListNode:
    def __init__(self,v):
        self.val=v
        self.next=None
class Solution:
    def FindKthToTail(self,head,k):
        p=head
        q=head

        while p and k:
            p=p.next
            k-=1
        if k>0:
            return
        while p:
            p=p.next
            q= q.next
        return q





if __name__ == '__main__':

    arr=[1,2,3,4]
    head=cur=ListNode(0)
    for v in arr:
        cur.next=ListNode(v)
        cur=cur.next
    solution=Solution()
    c=solution.FindKthToTail(head,1)
    print(c.val)


