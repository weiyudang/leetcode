# coding:utf-8

'''
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。


输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。

dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

'''


class Solution(object):
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        for i in range(len(nums)):
            a, b = b, max(b, a + nums[i])
        return b

    def massage2(self,nums):

        if not nums:
            return 0

        if len(nums)==1:
            return  nums[0]

        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])

        return dp[-1]



if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 1]
    print(solution.massage(nums))
    print(solution.massage2(nums))
