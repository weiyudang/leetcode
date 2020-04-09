# coding:utf-8
'''
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。


'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        size = len(nums)

        dp = [0] * (size+1)
        dp[0] = nums[0]
        dp[1] = nums[0]
        for i in range(1, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        # print(dp)
        return dp[size-1]


if __name__ == '__main__':
    solution = Solution()
    nums = [[1, 2, 3, 1],[],[3]]
    for i in range(len(nums)):
        print(solution.rob(nums[i]))
