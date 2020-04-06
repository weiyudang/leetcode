# coding:utf-8
'''
输入: [3,4,5,1,2]
输出: 1
你可以假设数组中不存在重复元素。
'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right=0,len(nums)-1
        while left<right:
            mid=left+right>>1
            if nums[mid]<nums[right]:
                right=mid
            else:
                left=mid+1
        return nums[left]



if __name__ == '__main__':
    solution = Solution()
    nums=[[3,4,5,1,2],[1,2,3,4]]
    index=0
    print(solution.findMin(nums[0]))

