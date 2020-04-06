# coding:utf-8

'''
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。

思路：
二分查找
mid>mid-1 and mid>mid+1

或者线性扫描



'''


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:

            mid = left + right >> 1
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

    def findPeakElement1(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return i - 1
        return len(nums)-1


if __name__ == '__main__':
    solution = Solution()
    nums = [[1, 2, 3, 1], [1, 2, 3, 4], [4, 3, 2, 1], [1, 2, 1, 3, 5, 6, 4], [1, 2, 1, 3, 5, 6, 4], [], [1]]
    for i in range(len(nums)):
        print(nums[i], ":", solution.findPeakElement1(nums[i]))

    print(solution.findPeakElement1([1, 2, 3]))
    print(range(3))
