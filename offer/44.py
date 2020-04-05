# coding:utf-8

'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''


class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None


class Solution(object):
    def deleteDuplication(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return dummy.next


if __name__ == '__main__':
    array = [1, 2, 3, 3, 4, 4, 5]
    phead = cur = ListNode(-1)
    for num in array:
        cur.next = ListNode(num)
        cur = cur.next
    # while phead:
    #     print(phead.val)
    #     phead=phead.next
