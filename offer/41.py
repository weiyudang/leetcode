#coding:utf-8


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        hashmap={}
        for i in range(len(numbers)):
            if numbers[i]  in hashmap:
                return  numbers[i]
            else:
                hashmap[numbers[i]]=1



