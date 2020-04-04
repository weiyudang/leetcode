#coding:utf-8
'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
1 1 2 3 5
思路1：递归
递归的边界条件
n<2 1
思路2：动态规划
无后效性

思路2:记忆搜索
类似于动态规划，只是空间复杂度较低，自下往上思考问题，f(n-1)+f(n-2)

类似的问题：
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
f(n)=2fn(n-1)

'''


class Solution(object):

    def Fibonacci(self,n):
        if n<2:
            return 1
        else:
            return self.Fibonacci(n-1)+self.Fibonacci(n-2)

    def Fibonacci_dp(self,n):
        if n<=2:
            return 1
        dp=[0]*(n)
        dp[0]=1
        dp[1]=1
        # range 是左闭，右开，如果要申请一个n
        for i in range(2,n):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]
    def Fibonacci_cc(self,n):
        if n<2:
            return 1
        a=b=1
        for i in range(2,n):
            a,b=b,a+b
        return b



if __name__ == '__main__':

    solution=Solution()
    print(solution.Fibonacci(3))
