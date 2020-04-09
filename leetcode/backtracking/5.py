# coding:utf-8
'''
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs2(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

    def dfs2(self, nums, path, res):
        if not nums:
            res.append(path[:])
        else:
            for i in range(len(nums)):
                path.append(nums[i])
                print(nums[i],len(nums),path)
                self.dfs2(nums[:i] + nums[i + 1:], path, res)
                print('---->>------')

                path.pop()
                print(nums[i],len(nums), path)
                # print('----++------')


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.permute(nums))
