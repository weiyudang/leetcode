# coding:utf-8
'''
统计一个数字在排序数组中出现的次数。

'''


def binary_search(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        elif arr[mid] < target:
            left = mid+1
        else:
            return True
    return False


def binary_search_recur(arr,target):
    n=len(arr)
    if n>0:
        mid=n//2
        if arr[mid]==target:
            return True
        elif arr[mid]>target:
            return binary_search_recur(arr[:mid],target)
        else:
            return  binary_search_recur(arr[mid+1:],target)
    return False







if __name__ == '__main__':
    arr = [1, 2, 2, 2, 3, 4, 5, 5, 5, 7]
    arr1=[1,2,3,4,5]
    print(binary_search(arr1,100))
    print (binary_search(arr,100))