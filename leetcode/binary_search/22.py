# coding:utf-8
'''
给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一样，优先选择数值较小的那个数。

输入: [1,2,3,4,5], k=4, x=3
输出: [1,2,3,4]

输入: [1,2,3,4,5], k=4, x=-1
输出: [1,2,3,4]

思路：
- 二分查找
'''


class Solution:
    def findClosestElements(self, arr, k, x):
        if not arr:
            return []
        if len(arr) < k:
            return arr
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]
        index = self.binaray_search(arr, x)
        print(index)
        left = index
        right = index
        while k:
            if abs(x - arr[left]) < abs(x - arr[right]):
                left -= 1
            else:
                right += 1
            k -= 1
        print(left, right)
        return arr[left:right]

    def binaray_search(self, arr, x):

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + right >> 1
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return mid


def binaray_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + right >> 1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binaray_search2(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + right >> 1
        # print(left, right, mid)
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return mid


class Solution2:
    def findClosestElements(self, arr, k, x):
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = l + r >> 1
            if arr[mid] >= x:
                r = mid
            else:
                l = mid + 1

        if l == 0:
            return arr[:k]
        elif l == len(arr) - 1:
            return arr[-k:]
        else:
            # 表示区间[i, j)现在在满足条件
            if arr[l] == x:
                i = l
                j = l + 1
            else:
                if x - arr[l - 1] <= arr[l] - x:
                    i = l - 1
                    j = l
                else:
                    i = l
                    j = l + 1
            while j - i < k:
                if i == 0:
                    j += 1
                    continue
                if j == len(arr):
                    i -= 1
                    continue
                if x - arr[i - 1] <= arr[j] - x:
                    i -= 1
                else:
                    j += 1
        return arr[i:j]


if __name__ == '__main__':
    solution = Solution()
    arr = [1, 1, 1, 10, 10]
    print(binaray_search2(arr, 3))
    print(solution.findClosestElements(arr, 1, 9))

    a={1:2,4:3}
    for k,v in a.items():
        print(k)
