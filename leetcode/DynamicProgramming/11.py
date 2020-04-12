# coding:utf-8
'''
标签：动态规划
遍历数组时计算当前最大值，不断更新
令imax为当前最大值，则当前最大值为 imax = max(imax * nums[i], nums[i])
由于存在负数，那么会导致最大的变最小的，最小的变最大的。因此还需要维护当前最小值imin，imin = min(imin * nums[i], nums[i])
当负数出现时则imax与imin进行交换再进行下一步计算
时间复杂度：O(n)O(n)

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。


'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        maxV = nums[0]
        imax = 1
        imin = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax=max(imax*nums[i],nums[i])
            imin=min(imin*nums[i],nums[i])
            maxV=max(maxV,imax)
            print(imax,imin)
        return maxV

if __name__ == '__main__':
    solution = Solution()
    nums=[[2,3,-2,4,-1],[-2,0,-1]]
    index=0
    print(solution.maxProduct(nums[index]))