# coding:utf-8
'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：
- 所有数字（包括 target）都是正整数。
- 解集不能包含重复的组合。

思路：
回溯+剪枝

控制迭代的此说：
target-i<0 则跳过
res[-1]>i 则跳过

'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        self.res = []
        self.dfs(candidates, target, [])
        return self.res

    def dfs(self, candidates, target, res):
        if target == 0:
            self.res.append(res)
        else:
            for i in candidates:
                if target - i < 0:
                    continue
                if len(res) >= 1 and res[-1] > i:
                    continue
                self.dfs(candidates, target - i, res + [i])


from typing import List


class Solution2:
    def combinationSum(self, candidates, target):
        size = len(candidates)
        if size == 0:
            return []

        # 剪枝是为了提速，在本题非必需
        candidates.sort()
        # 在遍历的过程中记录路径，它是一个栈
        path = []
        res = []
        # 注意要传入 size ，在 range 中， size 取不到
        self.__dfs(candidates, 0, size, path, res, target)
        return res

    def __dfs(self, candidates, begin, size, path, res, target):
        # 先写递归终止的情况
        if target == 0:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 或者使用 path.copy()
            res.append(path[:])
            return

        for index in range(begin, size):
            residue = target - candidates[index]
            # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
            # print(residue,candidates[index])
            if residue < 0:
                break
            path.append(candidates[index])

            # 因为下一层不能比上一层还小，起始索引还从 index 开始
            self.__dfs(candidates, index, size, path, res, residue)
            # print(path)
            path.pop()


if __name__ == '__main__':
    solution = Solution2()
    candidates = [[2, 3, 6, 7], [2, 3, 5]]
    target = [7, 8]
    '''
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
    ]
    '''
    index = 0
    print(solution.combinationSum(candidates[index], target[index]))
