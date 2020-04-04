# coding:utf-8
'''
输入两个链表，找出它们的第一个公共结点。（
注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
思路：首先要确定是两个链表的长度，然后长链表先走k步（k 是两个链表长度只差），然后短链表
再开始走，关键是确定k的值，假设两个链表同时遍历，短遍历完，则从长开始，长遍历完就从短的开始，这样，就间接的
求出k,而不许明确的计算k
'''


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead2 or not pHead1:
            return

        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1

        return p1
