# coding:utf-8
'''
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
示例 1:
s = "abc", t = "ahbgdc"

双指针法：
i，j  分别指向两个字符串的首位，如果相同则后移，否则j+=1
'''


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len = len(s)
        t_len = len(t)
        i = 0
        j = 0
        while i < s_len and j < t_len:

            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == s_len:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    s = "abx"
    t = "ahbgdc"
    print(solution.isSubsequence(s, t))
