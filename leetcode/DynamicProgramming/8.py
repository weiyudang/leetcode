# coding:utf-8


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            dp[0][0] = 0

        for i in range(1, n):
            if dp[0][i - 1] == 1 and obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                dp[0][i] = 0

        for i in range(1, m):
            if dp[i - 1][0] == 1 and obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                dp[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] =0
                else:
                    dp[i][j]= dp[i - 1][j]+dp[i][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    obstacleGrid = [[0, 1]]
    print(solution.uniquePathsWithObstacles(obstacleGrid))
