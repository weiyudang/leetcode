# coding:utf-8
'''
二叉树的构建
思路：
递归，从上到下的思考问题
首先要插入v 要判断根节点的是否为空，是则赋值，否则，分别检测左右子节点是否为空，为None赋值，否则，进入递归子结构

基本条件：是在保证二叉树的基础上，只有节点为None 才插入
'''


# class TreeNode(object):
#
#     def __init__(self,v):
#         self.val=v
#         self.left=None
#         self.right=None
#
#     def PrintTree(self):
#         print(self.val)


class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

    def insert(self, v):

        if self.val:
            if v < self.val:
                if self.left is None:
                    self.left = TreeNode(v)
                else:
                    self.left.insert(v)
            else:
                if self.right is None:
                    self.right = TreeNode(v)
                else:
                    self.right.insert(v)
        else:
            self.val = v

    def findv(self,v):

        if v<self.val:
            if self.left is None:
                return False
            return self.left.findv(v)
        elif v>self.val:
            if self.right is None:
                return False
            return self.right.findv(v)
        else:
            return True

    def PrintTree(self):
        '''

        :return: 中序遍历
        '''
        if self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()


if __name__ == '__main__':
    arr = [1, 2, 3,  5, 6, 7]
    tree = TreeNode(4)
    for num in arr:
        tree.insert(num)
    print("----")
    tree.PrintTree()
    k=10
    if tree.findv(10):
        print("is Found")
    else:
        print("not Found")
