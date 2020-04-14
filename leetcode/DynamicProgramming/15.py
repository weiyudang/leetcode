# coding:utf-8
import math


class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 3: return n - 1

        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

    def maxProduct(self, n):
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


if __name__ == '__main__':
    solution = Solution()
    num=10
    print(solution.cuttingRope(num))
    print(solution.maxProduct(num))
