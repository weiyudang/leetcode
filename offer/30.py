# coding:utf-8
'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)
中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
a
思路1：遍历一遍，将每个字符串出现的次数记录，第二次遍历就可以找出只出现一次的字符串
思路2:
'''


class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
        print(hashmap)
        index = -1
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                index = i
                break

        return index


if __name__ == '__main__':
    s = 'aabcbc'
    solution = Solution()
    print(solution.FirstNotRepeatingChar(s))
