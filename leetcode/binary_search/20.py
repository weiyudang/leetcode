# coding:utf-8
'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

输入: [1,3,4,2,2]
输出: 2

输入: [3,1,3,4,2]
输出: 3

思路：
1。 先排序O(nlogn) 再线性搜索O(n)
2. hashMap  O(n) 空间的复杂度 O(n)
3：弗洛伊德的乌龟和兔子（循环检测） leetcode(141，142)
4: 快慢指针

https://leetcode-cn.com/problems/find-the-duplicate-number/solution/xun-zhao-zhong-fu-shu-by-leetcode/


'''


class Solution(object):
    def findDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

    def findDuplicate2(self, nums):
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return num
            else:
                hashmap[num] = 1

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        理解以下思想
        """
        # 此题转换为链表找环的开始位置，前提条件告诉我们是一定有环
        # 根据floyd判圈办法，一个快指针一个慢指针，二者一定在环上相遇，设相遇点为M点，
        # 快是慢的速度的2倍，时间相同，设慢的距离为s，那么快的距离为2s
        # m为链表头距离环开始位置的距离，k为环开始位置到M点的距离, N为环长度
        # s = m + a*N +k, 2s = m + b*N +k，二者相减，s = (a-b)*N
        # 由此可见，慢指针走过的距离是环长的整数倍，即链表头到M点是环长的整数倍
        # 如果是1倍的话，把m截距离旋转到环上，跟环融合，那么链表头一定落在M点，
        # 即fast和slow都落在M点，那么二者到环开始位置距离相同，必然在此处相遇。
        # 如果是N倍（N>1）时，只不过slow指针多转几圈而已，后二者扔在此处相遇
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]  # next
            fast = nums[nums[fast]]  # next.next
            if slow == fast:
                break

        fast = nums[0]
        while True:
            if slow == fast:
                break
            slow = nums[slow]
            fast = nums[fast]

        return slow


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 4, 2, 2]
    nums2 = [3, 1, 5, 4, 2]
    index2 = [0, 1, 2, 3, 4]
    print(solution.findDuplicate2(nums))
