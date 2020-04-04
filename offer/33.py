# coding:utf-8
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转 leetcode 153
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
输入: [3,4,5,1,2]
输出: 1
思路：
1。
left right

left<mid 左区间是递增序列，最小值肯定在右区间
left>mid 右区间是递增序列，最小值肯定在左区间

思路二：
只需比较中间值与前后的关系
mid>mid+1 -> mid+1
mid<mid-1 ->


'''


def binary_search(arr):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[left] < arr[mid]:
            left = mid
        elif arr[left] > arr[mid]:
            right = mid
        else:
            return arr[right]


class Solution:
    def findMin(self, arr):
        if len(arr) == 1:
            return arr[0]
        left = 0
        right = len(arr) - 1
        if arr[left] < arr[right]:
            return arr[left]
        while left < right:
            mid = (left + right) // 2

            if arr[left] < arr[mid]:
                left = mid
            elif arr[left] > arr[mid]:
                right = mid
            else:

                return arr[right]

    def findMin2(self, arr):
        left = 0
        right = len(arr) - 1
        if arr[left] < arr[right]:
            return arr[left]

        while left < right:
            mid = left + (left - right) / 2
            if arr[mid] > arr[mid + 1]:
                return arr[mid + 1]
            if arr[mid - 1] > arr[mid]:
                return arr[mid]

            if arr[left] < arr[mid]:
                left = mid + 1
            else:
                right = mid - 1


if __name__ == '__main__':
    arr = [3, 4, 5, -1, 0, 1, 2]
    solution = Solution()
    print(solution.findMin(arr))
    arr = [3, 4, 5, 0, 1, 2]
    print(solution.findMin2(arr))
