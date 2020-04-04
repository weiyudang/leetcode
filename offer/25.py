# coding:utf-8
'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
思路：
1.最简单就是从头到位统计一遍，然后找到大于n//2 的数字，O(n)  空➖换时间
2.
'''


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        ''''''
        if not numbers:
            return

        hashmap = {}
        max_num = 0
        res = None
        for num in numbers:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
            if max_num < hashmap[num]:
                max_num = hashmap[num]
                res = num
        return res


if __name__ == '__main__':
    numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    hashmap = {}
    max_num = 0
    res = None
    for num in numbers:
        if num in hashmap:
            hashmap[num] += 1

        else:
            hashmap[num] = 1
        if max_num < hashmap[num]:
            res = num
    print(res)
