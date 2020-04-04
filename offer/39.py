# coding:utf-8
'''
k最近邻
我们有一个整形数组a，大小为n，里面的数字是按照由小到大排序的，无重复。
现在给一个查询数字x和召回数k，要求返回a中和x最接近的k个数字。

'''


def binary_search(arr, k):
    left = 0
    right = len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if abs(arr[mid] - k) < abs(arr[mid + 1] - k) and abs(arr[mid] - k) < abs(arr[mid - 1] - k):
            return mid
        if abs(arr[mid - 1] - k) < abs(arr[mid + 1] - k):
            right = mid
        else:
            left = mid

    return -1


def KNearestElements(data, x, k):
    index = binary_search(data, x)
    i = index - 1
    j = index + 1
    res = [data[index]]
    while k - 1:
        if data[i] <= data[j]:

            res.append(data[i])

            i -= 1
        else:
            res.append(data[j])
            j += 1
        k -= 1
    return res


def binary_search_k(arr, item):
    left = 0
    right = len(arr)
    while left < right:
        mid = left + right >> 1
        if arr[mid] >= item:
            right = mid
        else:
            left = mid + 1
        # print(arr[mid])
    return arr[mid]


if __name__ == '__main__':
    arr = [1, 2, 4,5, 6, 7, 10]
    # print(KNearestElements(arr, 3, 2))
    # print(binary_search(arr, 3))
    print(binary_search_k(arr,3))
