# coding:utf-8
'''
剪绳子
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
leetcode(14)
https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/
两种方式：
1。记忆搜索
2。公式证明，最优长度为3，再对不能切分成3的进行单独处理
'''


def maxProduct(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    products = [0] * (n + 1)
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3
    _max_ = 0
    for i in range(4, n + 1):
        _max = 0
        for j in range(1, i // 2 + 1):
            prod = products[j] * products[i - j]
            if _max < prod:
                _max = prod
        products[i] = _max

    return products[n]


import math


class Solution:
    def cuttingRope(self, n):
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)
