# coding:utf-8
'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

思路：
和1相比 只是数组有重复

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

'''


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        begin = 0
        size = len(candidates)
        candidates = sorted(candidates)
        res = []
        self.dfs(candidates, begin, size, [], res, target)
        return res

    def dfs(self, candidates, begin, size, path, res, target):
        if target == 0:
            res.append(path[:])
        else:
            for i in range(begin, size):
                if target - candidates[i] < 0:
                    continue
                if i > begin and candidates[i - 1] == candidates[i]:
                    continue
                path.append(candidates[i])
                self.dfs(candidates, i + 1, size, path, res, target - candidates[i])
                path.pop()


if __name__ == '__main__':
    solution = Solution()
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(solution.combinationSum2(candidates, target))
    path = [1, 2, 3, 4]
    c=path
    c1=path[:]
    path.pop()
    print(c1)
    print(c)
