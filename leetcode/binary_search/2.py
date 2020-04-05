# coding:utf-8

'''
X 的平方根

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

'''


class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        left, right = 2, x // 2
        while left < right:
            pivot = (left + right) // 2
            num = pivot * pivot
            print(left, right)
            if num < x:
                left = pivot + 1
            elif num > x:
                right = pivot
            else:
                return pivot
        return left - 1  # 最后left 与right 是相等


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(20))
    array = [1, 3, 5, 7]
