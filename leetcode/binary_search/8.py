# coding:utf-8
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 
[3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

输入：[3,4,5,1,2]
输出：1


输入：[2,2,2,0,1]
输出：0

典型的二分查找的变种

思路：
left ,right 分别指向 数组的首位位置
mid=left+(right-left)//2

1。if numbers[mid]<numbers[right] 则说明 mid右侧是有序的数组，找最小值去左侧找,由于可能会是2，2，2，0，1 这种数组，需要用等号判断
2。if numbers[mid]>numbers[right] 则说明 mid 左侧是升序列排列的，所以要从🈶右侧找

3. 如果numbers[left]<numbers[right] 则 left 就是最小值

需要注意的是，边界条件，1 left=mid+1  right=mid-1  需要left<=right 式样的二分查重



'''


class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if len(numbers) == 1:
            return numbers[0]
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = left + (right - left) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right -= 1

        return numbers[left]


if __name__ == '__main__':
    solution = Solution()
    numbers = [3, 4, 5, 1, 2]
    numbers1 = [2, 2, 2, 0, 1]
    numbers2 = [1, 1, 1]
    numbers3 = [3, 1, 3]
    print(solution.minArray([ 5, 6, 7, 0, 1,2,3]))
