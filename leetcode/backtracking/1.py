# coding:utf-8
'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

思路：
回溯法

'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        hashmap = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        s = []
        digits = int(digits)
        while digits:
            s.append(hashmap[digits % 10])
            digits = digits // 10
        self.res = []
        self.dfs(s[::-1], '')
        return self.res

    def dfs(self, s, path):
        if not s:
            self.res.append(path)
        else:
            for i in s[0]:
                self.dfs(s[1:], path + i)


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations('234'))
