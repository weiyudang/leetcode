# coding:utf-8

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.helper(pRoot.right, pRoot.left)

    def helper(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is  None or left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
