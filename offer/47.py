# coding:utf-8
'''
请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，
从而使得内存中建立起来的二叉树可以持久保存。
序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，
序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。
主要的关键点是是每次递归都有返回值
反序列化的时候的pop
'''


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

    def findv(self, v):
        if v < self.val:
            self.left.findv(v)
        elif v > self.val:
            self.right.findv(v)
        else:
            return True

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()


class Solution:

    def Serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += '#!'
            else:
                string += str(root.val) + '!'
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string

        return rserialize(root, '')

    def Deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == '#':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split('!')
        root = rdeserialize(data_list)
        return root


class Solution1:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here

        self.res = []
        self.inoder(pRoot)
        if len(self.res) < k:
            return None
        else:
            return self.res[k-1]

    def inoder(self, root):
        if not root:
            return None
        if root.left:
            self.inoder(root.left)
        self.res.append(root.val)
        if root.right:
            self.inoder(root.right)


if __name__ == '__main__':
    arr = [2, 3, 1, 6, 7, 5]
    root = TreeNode(4)
    for num in arr:
        root.insert(num)

    root.PrintTree()
    # print(root.Serialize())
    # code = Solution()
    # ser_str = code.serialize(root)
    # print(ser_str)
    # print(code.deserialize(ser_str))
    sol = Solution1()
    print('----')
    print(sol.KthNode(root, 1))
    print(sol.res)
