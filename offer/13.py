# coding:utf-8

'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
思路：
递归的进行判断
B是A的子结构首先要满足
1.B 的根节点和A的跟节点相同
2.左右子树都必须满足节点都得相同
递归的思想 从上倒下，然后直至到达叶子节点
'''


class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        res=False
        if pRoot1.val == pRoot2.val:
            res = self.isSubtree(pRoot1, pRoot2)
        if not res and pRoot1.left:
            res = self.isSubtree(pRoot1.left, pRoot2)
        if not res and pRoot1.right:
            res = self.isSubtree(pRoot1.right, pRoot2)
        return res

    def isSubtree(self, proot1, proot2):
        if not proot2:
            return True
        if not proot1:
            return False
        if proot1.val != proot2.val:
            return False

        return self.isSubtree(proot1.left, proot2.left) and \
               self.isSubtree(proot1.right, proot2.right)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
