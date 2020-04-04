# coding:utf-8

class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0

        return max(self.TreeDepth(pRoot.right), self.TreeDepth(pRoot.right)) + 1

    def TreeDepth_norecur(self, pRoot):
        if not pRoot:
            return 0

        stack = []
        if pRoot:
            stack.append((1, pRoot))

        depth = 0
        while stack:
            current_depth, root = stack.pop()
            if root:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth
