# coding:utf-8
'''
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
思路：
使用深度优先遍历和回溯法
需要判断边界条件,如果左右子树都为空

'''


class Solution:
    def __init__(self):
        self.res = []

    def FindPath(self, root, expectNumber):
        if not root:
            return []

        self.subPath(root, [], expectNumber)
        return self.res

    def subPath(self, root, path, expectNumber):
        if not root.left and not root.right:
            if root.val == expectNumber:
                path.append(root.val)
                self.res.append(path)

        if root.left:
            self.subPath(root.left, path + [root.val], expectNumber - root.val)
        if root.right:
            self.subPath(root.right, path + [root.val], expectNumber - root.val)
