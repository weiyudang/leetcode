# coding:utf-8
'''
根节点的值大于其左子树中任意一个节点的值，小于其右节点中任意一节点的值，这一规则适用于二叉查找树中的每一个节点。
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
思路：
二叉搜索树中任意一颗子树都是左小右大
后边的遍历结果右一个特征，根节点的值肯定是最后的一个
那么根据这个思路，对于任意子树前面肯定小于根节点，后面肯定大于根节点，否则不是二叉搜索树的遍历结果
进行递归的判断，
假如最后只有两个节点的话则判断完成

1,3,2,5,7,6,4
'''


class Solution:

    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False

        return self.isBST(sequence)

    def isBST(self, sequence):
        if len(sequence) < 2:
            return True

        root = sequence[-1]
        i = 0

        while sequence and sequence[i] < root:
            i += 1
        j = i
        while sequence[j] > root:
            j += 1
        if j < len(sequence) - 1:
            return False
        else:
            return self.isBST(sequence[:i]) and self.isBST(sequence[i + 1:-1])


if __name__ == '__main__':
    pass
