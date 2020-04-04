# coding:utf-8
'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
思路：二叉搜索树的特征是左子树都小于根节点，右子树都大于根节点
二叉搜索树的中序遍历是有序的
1。 可以首先进行中遍历，然后再插入链表
2。根据直接再后序遍历中进行
方式与链表的插入类似

'''


class TreeNode:


    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.listTail = None
        self.listHead = None

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.Convert(pRootOfTree.left)

        if self.listHead:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead
