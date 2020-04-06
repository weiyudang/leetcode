# coding:utf-8
'''
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

思路：
二分查找的变种
i,j 指向左下角
target>matrix[i][j] 则target 肯定存在与该行，则j+=1 否则肯定在i-=1
临界条件：
matrix=[] return False
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = len(matrix) - 1
        col = len(matrix[0])
        j = 0
        i = row
        while i >= 0 and j < col:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 17
    print(solution.searchMatrix(matrix, target))
