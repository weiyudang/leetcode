# coding:utf-8
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4


思路1：
- 确定旋转的index
- 分别对左有序和右有序进行查找
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        rotate_index = self.findPivote(nums)
        print(rotate_index)
        if nums[-1] >= target:
            index = self.binaray_search(nums[rotate_index:], target)
            if index != -1:
                index = rotate_index + index
            return index
        else:
            return self.binaray_search(nums[:rotate_index], target)

    def binaray_search(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + right >> 1
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1

    def findPivote(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + right >> 1
            print(left, right)
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return left


if __name__ == '__main__':
    solution = Solution()
    nums = [1]
    target = 1
    solution.search(nums, 1)
