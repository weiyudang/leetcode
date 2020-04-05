# coding:utf-8
'''
给定两个数组，编写一个函数来计算它们的交集。
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]

思路：
可以使用hashmap 首先扫描第一个数组，再扫描第二个数组，复杂度O(M+N) 空间复杂度O(min(M,N))

或者是双指针法，首先对数组进行排序，O(nlogn+mlogm)
- 对数组 nums1 和 nums2 排序。
- 初始化指针 i，j 和 k 为 0。
- 指针 i 指向 nums1，指针 j 指向 nums2：
  如果 nums1[i] < nums2[j]，则 i++。
  如果 nums1[i] > nums2[j]，则 j++。
  如果 nums1[i] == nums2[j]，将元素拷贝到 nums1[k]，且 i++，j++，k++。
返回数组 nums1 前 k 个元素。

'''


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        hashmap = {}

        for num in nums1:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        for num in nums2:
            if num in hashmap and hashmap[num] != 0:
                res.append(num)
                hashmap[num] -= 1

        return res


class Solution1(object):

    def helper(self, nums1, nums2):
        res = []
        hashmap = {}
        for num in nums1:
            hashmap[num] = 1
        for num in nums2:
            if num in hashmap:
                res.append(num)
        return res

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if len(nums1) > len(nums2):
            return self.helper(nums2, nums1)
        else:
            return self.helper(nums1, nums2)


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    solution = Solution()
    print(solution.intersection(nums1, nums2))
