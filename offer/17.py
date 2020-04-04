#coding:utf-8

'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

栈相关的问题一般都需要辅助栈
含有min函数的最小栈的整体思路，将最小值按照压入栈的顺序依次进栈，如果小于最小栈的栈顶，
则插入，否则插入栈顶元素，重复插入
这里的有一个重复插入的操作，
如果不重新插入的话，则是弹出时，需要作出判断
条件为：如果弹出的元素是否等于最小栈的栈顶，是则最小栈不弹出，否则弹出
'''

class Solution:
    def __init__(self):
        self.minStack=[]
        self.stack=[]

    def push(self,v):

        if not self.minStack or  v<self.minStack[-1]:
            self.minStack.append(v)
        else:
            self.minStack.append(self.minStack[-1])

        self.stack.append(v)

    def pop(self):
        if self.stack:
            self.minStack.pop()
            self.stack.pop()



    def top(self):
        if self.stack:
            return self.stack[-1]

    def min(self):
        if self.minStack:
            return self.minStack[-1]



if __name__ == '__main__':
    arr=[2,6,3,4,1,5]
    solution=Solution()
    for num in arr:
        solution.push(num)

    for num in solution.minStack:
        print(num)



