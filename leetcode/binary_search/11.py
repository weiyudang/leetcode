# coding:utf-8
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false

近阶：
这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
答：不会影响时间复杂度，时间复杂度都是Olog(n)
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/zai-javazhong-ji-bai-liao-100de-yong-hu-by-reedfan/
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        pivot_index = self.findPivote(nums)
        print(pivot_index)
        if target <= nums[-1]:
            return self.binary_search(nums[pivot_index:], target)
        else:
            return self.binary_search(nums[:pivot_index], target)

    def binary_search(self, nums, target):

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid-1
            else:
                return True
        # 返回下界
        return False

    def findPivote(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:

            mid = left + right >> 1
            # print(left, right)
            # print(mid)
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return left


if __name__ == '__main__':
    solution = Solution()
    nums = [1]
    target = 1
    print(solution.search(nums, target))
    print(nums[0:])