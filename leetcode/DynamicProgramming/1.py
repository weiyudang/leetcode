# coding:utf-8


'''

这道题用动态规划的思路并不难解决，比较难的是后文提出的用分治法求解，但由于其不是最优解法，所以先不列出来
动态规划的是首先对数组进行遍历，当前最大连续子序列和为 sum，结果为 ans
如果 sum > 0，则说明 sum 对结果有增益效果，则 sum 保留并加上当前遍历数字
如果 sum <= 0，则说明 sum 对结果无增益效果，需要舍弃，则 sum 直接更新为当前遍历数字
每次比较 sum 和 ans的大小，将最大值置为ans，遍历结束返回结果
时间复杂度：O(n)


输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max, global_max = nums[0], nums[0]
        for nu in nums[1:]:
            local_max = max(nu, local_max + nu)
            global_max = max(global_max, local_max)
        return global_max


if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums))
