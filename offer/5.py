# coding:utf-8
'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
思路：
队列是它只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作，和栈一样，
队列是一种操作受限制的线性表。进行插入操作的端称为队尾，进行删除操作的端称为队头。
栈是先进后出

push  直接放栈顶 stack1
pop  从stack1以此推入stack2,然后从从stack2 弹出，然后再依次将stack2 倒入stack1 这样保证
stack1保持插入的顺序
'''


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        res = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return res


if __name__ == '__main__':
    solution=Solution()
    solution.push(100)
    solution.push(200)
    solution.push(300)
    print(solution.pop())
