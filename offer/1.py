# coding:utf-8

'''
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):

        # write code here
        col=len(array)-1
        row=len(array[0])
        i=col
        j=0
        while j<row and i>=0:
            if array[i][j]<target:
                j+=1
            elif array[i][j]>target:
                i-=1
            else:
                return True
        return False


if __name__ == '__main__':
    array=[[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    target=7

    solution=Solution()
    array=[[]]
    print(solution.Find(100,array))

