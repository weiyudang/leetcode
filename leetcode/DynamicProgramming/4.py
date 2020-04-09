# coding:utf-8
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 2
        for i in range(2, n):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(4))
