# coding:utf-8
'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
1.思路简单的莫过于循环求最小，循环k 次，时间复杂度为O(nk)
2. 使用快排的思路，快速排序每次将数据分
快速排序：一顿人分两半，小的在右大的在左，然后递归
它的基本思想是：通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。 [1]
冒泡： 相邻的比较
选择:第一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，
然后再从剩余的未排序元素中寻找到最小（大）元素，
'''


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        return quick_sort(tinput, 0, len(tinput), k)


def quick_sort(array, left, right, k):
    if left > right:
        return
    if len(array) < k and k <= 0:
        return []
    low = left
    high = right
    base = array[left]
    while left < right:
        while left < right and array[right] > base:
            right -= 1
        array[left] = array[right]
        # print(numbers)
        while left < right and array[left] < base:
            left += 1
        array[right] = array[left]
        # print(numbers)
    array[left] = base
    if left != k - 1:
        if left > k - 1:
            quick_sort(array, low, left - 1, k)
        if left < k - 1:
            quick_sort(array, left + 1, high, k)
    return array[:k]


def quickSort(numbers,left,right):
    if left>right:
        return
    low=left
    high=right
    base=numbers[low]

    while left<right:
        while left<right and numbers[right]>base:
            right-=1
        numbers[left]=numbers[right]
        while left<right and numbers[left]<base:
            left+=1
        numbers[right]=numbers[left]
    numbers[left]=base

    quickSort(numbers,left+1,high)
    quickSort(numbers,low,left-1)



if __name__ == '__main__':
    numbers = [4, 5, 1, 6, 2, 7, 3, 0]

    i = 0
    k = 3
    j = len(numbers)
    for i in range(k):
        index = i
        while i < j:
            if numbers[index] > numbers[i]:
                numbers[index], numbers[i] = numbers[i], numbers[index]
            i += 1

    numbers = [4, 5, 1, 6, 2, 7, 9, 0]
    print(quick_sort(numbers, 0, len(numbers) - 1, 3))
    numbers = [4, 5, 1, 6, 2, 7, 9, 0]
    quickSort(numbers,0,len(numbers)-1)
    print(numbers)
