#coding:utf-8
'''
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
思路：
1.编列链表将链表的node的值，以此放入栈中
2.栈为先进后出，从栈顶以此pop 即可

'''
class ListNode(object):
    def __init__(self,v):
        self.val=v
        self.next=None

class Solution(object):

    def printListFromTailToHead(self,listNode):
        stack=[]
        cur=listNode
        while cur:
            stack.append(cur.val)
            cur=cur.next
        res=[]
        while stack:
            res.append(stack.pop())
        return res










if __name__ == '__main__':

    arr=[1,2,3,4]
    head=cur=ListNode(0)
    for num in arr:
        cur.next=ListNode(num)
        cur=cur.next

    # print(head.next)
    listNode=head.next
    stack=[]
    cur=listNode
    # while cur:
    #     stack.append(cur.val)
    #     cur=cur.next
    #
    # print('____')
    # for i in stack[::-1]:
    #     print(i)
    #

    solution=Solution()
    print(solution.printListFromTailToHead(cur))




