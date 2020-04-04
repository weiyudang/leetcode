#coding:utf-8
'''
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,
他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,
问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
思路，可以当成一个动态规划问题
如果前面的数字+当前的数字，比当前的数字小的化，那就前面的对最大值的贡献
[1,2,-4,4]
[1,2] => 3
1,2,-4=>-1
- 对4 没有贡献，所以4的连续子数组最大值为4
所以涉及局部最大和全局最大的

'''


class Solution(object):
    def FindGreatestSumOfSubArray(self, array):
        local_max,global_max=array[0],array[0]
        for i in range(1,len(array)):
            local_max=max(local_max+array[i],array[i])
            global_max=max(global_max,local_max)
        return global_max







if __name__ == '__main__':
    arr=[6, -3, -2, 7, -15, 1, 2, 2]

    solution=Solution()
    print(solution.FindGreatestSumOfSubArray(arr))


