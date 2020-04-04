# coding:utf-8
'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。

思路1：
递增序列和为S 但要求输出的乘积为最小，最小一般是j-i 是差是最大的
1，2，3，4，5

双指针第一次找的就是乘积最小的
'''


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return

        i = 0
        j = len(array)-1
        res = []
        while i < j:
            if array[j] > tsum:
                j -= 1
                continue
            cursum = array[i] + array[j]
            if cursum == tsum:
                return [array[i], array[j]]
            elif cursum < tsum:
                i += 1
            else:
                j -= 1
        return []


if __name__ == '__main__':
    solution=Solution()
    print(solution.FindNumbersWithSum([1,2,3,4,5],5))

