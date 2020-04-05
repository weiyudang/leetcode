# coding:utf-8

'''
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
思路：
双指针法
left right
sum=left+right
- sum==target return left,right
- sum>target right-=1
- sum>target  left+=1

折中的方式也可以通过二分查找，确定排序数组中刚好大于target 的下标，从小于下表的开始，但是在只是正整数的前提下
'''


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            tsum = numbers[left] + numbers[right]
            if tsum == target:
                return [left, right]
            elif tsum > target:
                right -= 1
            else:
                left += 1
        return []


def binary_search(numbers, target):
    left, right = 0, len(numbers)
    while left < right:
        mid = left + (right - left) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9

    print(binary_search(numbers, target))
