# coding:utf-8

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""
"""
思路：
双指针法
i=1,j=z
func(i,j)>z  j-=1
func(i,j)<z i+=1
func(i,j)=z 则不可能存在有数x 与i,j func只有等于z 所以i-=1 j-=1

边界条件为：i<=z and j>=1
因为假如z=2 输出应该是1，1 

如果不要求顺序，则边界条件可以为i<=j  if!=j res.append([j,i])
"""


class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        i, j = 1, z
        res = []
        while i <= z and j>=1:
            tres = customfunction.f(i, j)
            if tres > z:
                j -= 1
            elif tres < z:
                i += 1
            else:
                res.append([i, j])
                i+=1
                j-=1
        return res


if __name__ == '__main__':
    solution = Solution()
