# coding:utf-8
'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        else:
            for i in range(len(nums)):
                if i + 1 < len(nums) and nums[i] == nums[i + 1]: # 如果i==i+1 则跳过
                    continue
                self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2]
    print(solution.permuteUnique(nums))
