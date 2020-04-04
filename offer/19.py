# coding:utf-8
'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
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


def preorder(root):
    if not root:
        return None
    print(root.val)
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)


def preorder_norecur(root):
    '''
    非递归的方式实现树的前序遍历
    :param root:
    :return:
    '''
    stack = []
    while stack or root:
        while root:
            print(root.val)
            stack.append(root)
            root = root.left
        root = stack.pop()
        root = root.right


def midorder(root):
    if not root:
        return None
    midorder(root.left)
    print(root.val)
    midorder(root.right)


def midoder_norecur(root):
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        print(root.val)
        root = root.right


def postorder(root):
    if not root:
        return None

    postorder(root.left)
    postorder(root.right)
    print(root.val)

def postoder_norecur(root):
    pass



def bfs(root):
    if not root:
        return None
    stack = [root]
    res = []
    while stack:
        tmplist = []
        tmp = []
        for node in stack:
            tmplist.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            stack = tmp
        res.append(tmplist)
    return res


def maxDepth(root):
    '''
    recur
    :param root:
    :return:
    '''
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


def maxDepth_norecur(root):
    '''
    非递归的实现
    :param root:
    :return:
    '''
    if not root:
        return 0

    stack = [root]
    depth = 0
    while stack:
        res = []
        for node in stack:
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.left)
            if res:
                depth += 1
        stack = res
    return depth


if __name__ == '__main__':
    arr = [2, 3, 1, 6, 7, 5]
    root = TreeNode(4)
    for num in arr:
        root.insert(num)
    print('----')
    root.PrintTree()
    print("preorder")
    preorder(root)
    # 4,2,1,3,6,5,7
    print(bfs(root))
    # [[4], [2, 6], [1, 3, 5, 7]]
    print(maxDepth_norecur(root))
    print('----')
    # preorder_norecur(root)

    # midorder(root)
    # midoder_norecur(root)
    postorder(root)
    #1,3,2,5,7,6,4

