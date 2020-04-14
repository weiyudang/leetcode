# coding:utf-8
'''
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编
写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)



 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1

输入: n = 10
 输出：4
 解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1


思路：
1-->1
2——>1.1
3-->1.1.1
4-->1.1.1.1
5-->1.1.1.1,5
6--> 6-1 6-5
7--> 7-1 7-5
'''


class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        pass


def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    #             print(i)
    if dp[amount] > amount:
        return -1

    return dp[amount]

coins = [1, 2, 5, 7, 10]
coinChange(coins, 6)

if __name__ == '__main__':
    solution = Solution()

