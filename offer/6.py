# coding:utf-8
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

思路1:
最简单暴力的是遍历一遍复杂读是O(n)
思路2：
[3, 4, 5, 1,2]
利用二分查找
low high
if low<mid 说明左边是是递增序列，最小值肯定在右边 left=mid
if low>mid  说明最小值肯定是在左边，右边必然是递增的序列
如果high low 相邻，最小值肯定是high

'''


class Solution(object):
    def minNumberInRotateArray(self, rotateArray):
        minv = float('inf')

        for num in rotateArray:
            if num < minv:
                minv = num
        return minv

    def binary_search(self, rotateArray):
        low=0
        high=len(rotateArray)
        while rotateArray[low]>rotateArray[high]:
            if high-low==1:
                mid=high
                break
            mid=(left+right)//2
            if rotateArray[left]<=rotateArray[high]:
                left=mid
            else:
                right=mid
        return rotateArray[mid]




if __name__ == '__main__':
    arr = [2,3, 4, 5, 1]

    # minv = float('inf')
    # for num in arr:
    #     if minv > num:
    #         minv = num
    # print(minv)


    left = 0
    right = len(arr)-1
    while left< right:
        mid = (left + right) // 2
        if arr[left] < arr[mid]:
            left = mid+1
        elif arr[left] > arr[mid]:
            right = mid

    # print(left,right)
    print(arr[left])
    # solution=Solution()
    # print(solution.binary_search(arr))
