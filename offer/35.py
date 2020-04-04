# coding:utf-8
'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
思路：
当只有一个数字的只出现一次的时候，数据遍历异或即可得出该值
但是当有两个的出现一次的时候，可以将最后异或的值，按照最近的一个1进行区分
'''


def indexBit(num):
    i = 0
    while num:
        if num & 1 == 1:
            break
        else:
            num = num >> 1
            i += 1
    return i


def isBit(num, move_):
    num = num >> move_
    return num & 1


class Solution:

    def FindNumsAppearOnce(self, arr):

        if not arr:
            return

        base = 0
        for i in arr:
            base = base ^ i
        index1 = indexBit(base)
        res1 = 0
        res2 = 0
        for i in arr:
            if isBit(i, index1):
                res1 = res1 ^ i
            else:
                res2 = res2 ^ i

        return [res1, res2]


if __name__ == '__main__':

    arr = [2, 3, 2, 3, 4, 4, 5, 6]
    base = 0
    for i in arr:
        base = base ^ i
    print(base)
    print(5 ^ 6)
    print(isBit(4, 2))
    print('----')
    for i in arr:
        if isBit(i, 1):
            print(i)
