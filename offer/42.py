# coding:utf-8
'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
如果当前字符流没有存在出现一次的字符，返回#字符。

思路：
用hashmap 保存字符的出现的次数，
用s保存是字符的顺序，然后查找顺序查找第一个出现一次的字符
'''


class Solution:
    # 返回对应char
    def __init__(self):
        self.s = []
        self.hashmap = {}

    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.hashmap[i] == 1:
                return i
        return "#"

    def Insert(self, char):
        # write code here
        self.s.append(char)
        if char in self.hashmap:
            self.hashmap[char] += 1
        else:
            self.hashmap[char] = 1


if __name__ == '__main__':
    s = "google"
    solution=Solution()
    for i in s:
        solution.Insert(i)
        print(i,solution.FirstAppearingOnce())
