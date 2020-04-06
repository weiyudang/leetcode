# coding:utf-8

'''
给定一个含有 n 个正整数的数组和一个正整数 s ，
找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

思路
双指针法
i，j  sum(i,j) 表示i-j 之间的，如果小于s  j+=1 如果大于tsum-nums[i]  如果 等于

滑动窗口
'''


class Solution:
    def minSubArrayLen(self, s, nums):
        l = total = 0
        ans = len(nums) + 1
        for r in range(len(nums)):
            total += nums[r]
            while total >= s:
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if ans == len(nums) + 1 else ans


if __name__ == '__main__':
    solution = Solution()
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(solution.minSubArrayLen(s, nums))
