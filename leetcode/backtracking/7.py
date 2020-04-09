# coding:utf-8

'''
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。

输入: n = 3, k = 3
输出: "213"

'''


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        nums = range(1, n + 1)
        self.dfs(nums, [], res)

        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


class Solution2:
    def getPermutation(self, n, k):
        factorials, nums = [1], ['1']
        for i in range(1, n):
            # generate factorial system bases 0!, 1!, ..., (n - 1)!
            factorials.append(factorials[i - 1] * i)
            # generate nums 1, 2, ..., n
            nums.append(str(i + 1))

        # fit k in the interval 0 ... (n! - 1)
        k -= 1

        # compute factorial representation of k
        output = []
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]

            output.append(nums[idx])
            del nums[idx]

        return ''.join(output)


if __name__ == '__main__':
    solution = Solution()
    print(solution.getPermutation(3, 3))
