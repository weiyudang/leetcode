# coding:utf-8

'''
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。


'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        inf = int(1e9)
        min_price = inf
        profit = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            profit = max(profit, prices[i] - min_price)
        return profit


if __name__ == '__main__':
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    #     5
    print(solution.maxProfit(prices))
