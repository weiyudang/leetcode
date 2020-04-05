# coding:utf-8

'''
统计一个数字在排序数组中出现的次数。
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

思路是先二分查找，在上下遍历
三种思路：
思路1： 首先用二分查找确定target 的下届或者上届，然后线性搜索，
思路2； 分别进行二分查找target 的上下界限，然后去求差
思路3： target+0.5 和target -0.5 分别确定上下界，时间复杂度与思路2相同

https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/pu-tong-er-fen-cha-zhao-ji-ke-jie-jue-shuang-bai-b/
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        # if len(nums) == 1:
        #     if nums[0] == target:
        #         return nums[0]
        #     else:
        #         return 0

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # print(left, right)
            # 注意这里是小于，导致最终的left 为等于target 的最小下标，如果是等于 则最终的与target 相等的最大下标
            if nums[mid] < target:  # 是上届还是下届，关键是小于等于还是小于，小于确定的是下界，小于等于是确定是上界
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return 0
        else:
            count = 0
            while left < len(nums) and nums[left] == target:
                left += 1
                count += 1

        return count

    @classmethod
    def binary_search(cls, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:

            mid = left + right >> 1
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        return left

    def search2(self, nums, target):
        if not nums:
            return 0
        upper = self.binary_search(nums, target + 0.5)
        lower = self.binary_search(nums, target - 0.5)
        return upper - lower


if __name__ == '__main__':
    solution = Solution()
    cases = [[5, 7, 7, 8, 8, 8, 10], [5, 7, 7, 8, 8, 10], [1]]
    targets = [19, 6, 1]
    index = 0
    print(solution.search2(cases[index], targets[index]))
