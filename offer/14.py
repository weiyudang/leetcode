#coding:utf-8

'''
操作给定的二叉树，将其变换为源二叉树的镜像。

'''
class TreeNode:
    def __init__(self,v):
        self.val=v
        self.left=None
        self.right=None

class Solution:

    def Mirror(self,root):
        if not root:
            return
        root.left,root.right=self.Mirror(root.right),self.Mirror(root.left)
        return root




