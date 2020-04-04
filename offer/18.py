# coding:utf-8
'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
思路：
主要是临界条件的判断
遍历序列，依次进栈，如果栈顶元素等于压栈序列则弹出，否则继续遍历，直到遍历完成，如果压栈序列
为空则返回true
'''


class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV:
            return False

        stack = []
        for i in pushV:
            stack.append(i)
            while popV and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)

        if not popV:
            return True
        else:
            return False
