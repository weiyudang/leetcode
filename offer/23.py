# coding:utf-8
'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
思路：
这是一个经典dfs 题目，利用回溯的方法找到全排列，并完成去除重复和字典排序
大致思想便是，先确定第i个字符（从i到最后完成遍历枚举），然后对i+1:N-1个字符递归使用全排列（缩小范围），这便是dfs
只要每一层确定的字符不一样，那么便不会出现重复元素，换句话说，只要每一次递归枚举确定i元素时，不出现重复的即可，
这可用set实现，这比上述方法，提前去重，避免了后序很多无谓的递归。
https://blog.csdn.net/zjxxyz123/article/details/79709240
'''


class Solution:
    def Permutation(self, ss):
        if not ss:
            return ss

        self.res = []
        self.dfs(ss, '')
        return self.res

    def dfs(self, ss, path):
        if not ss:
            self.res.append(path)
        hashmap=dict()
        for i in range(len(ss)):
            if ss[i] not in hashmap:
                hashmap[ss[i]]=1
                self.dfs(ss[:i] + ss[i + 1:], path + ss[i])






if __name__ == '__main__':
    ss = 'aa'
    solution = Solution()
    print(solution.Permutation(ss))
    # arr=['a','b','c']
    # print(solution.permute(arr))
#