#coding:utf-8
'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。
'''

class Solution(object):

    def replaceSpace(self,s):
        res=''
        for c in s:
            if c==" ":
                c="%20"
            res+=c
        return res


if __name__ == '__main__':
    s="We Are Happy"
    s=''
    solution=Solution()
    print(solution.replaceSpace(s))


