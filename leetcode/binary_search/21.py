# coding:utf-8
'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明：
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
'''


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_upper = 0
        for i in range(len(nums)):
            pivot = i
            cnt = 1
            for j in range(i, len(nums)):
                if nums[j] > nums[pivot]:
                    cnt += 1
                    pivot = j
            if max_upper < cnt:
                max_upper = cnt
        return max_upper


if __name__ == '__main__':
    solution = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [10, 9, 2, 5, 3, 4]
    #   输出: 4
    #   [2,3,7,101]，它的长度是 4。
    max_upper = 0
    for i in range(len(nums)):
        pivot = i
        cnt = 1
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[pivot]:
                cnt += 1
                pivot = j
        if max_upper < cnt:
            max_upper = cnt

    print(max_upper)
    print(range(1, 3))
    # print(solution.lengthOfLIS(nums))
