# coding:utf-8
'''
稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。
输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
输出：-1
说明: 不存在返回-1。

输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
输出：4

字符比较（character comparison）是指按照字典次序对单个字符或字符串进行比较大小的操作，一般都是以ASCII码值的大小作为字符比较的标准。

字符串比较的时候，字符串的大小是从最左边第一个字符开始比较，大者为大，小者为小，若相等，则继续比较后面的字符；

比如ABC与ACDE比较，第一个字符相同，继续比较第二个字符，由于第二个字符是后面一个串大，所以不再继续比较，结果就是后面个串大。再如ABC与ABC123比较，比较三个字符后第一个串结束，所以就是后面一个串大。

思路：
二分查找与线性搜索

left,right=0,len(words)-1  分别指向首位字符串，线性搜索不为空的字符串，然后求mid ，中位也向前线性搜索
不为空的字符串，再使用二分查找即可

'''


class Solution(object):
    def findString(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        left, right = 0, len(words)-1
        while left <= right:
            while left < right and words[left] == "":
                left += 1
            while left < right and words[right] == "":
                right -= 1
            mid = (left + right) // 2
            print(left,right)
            while mid > left and words[mid] == "":
                mid -=1
            if words[mid] == s:
                return mid
            elif words[mid] < s:
                left = mid + 1
            else:
                right = mid-1

        return -1


if __name__ == '__main__':
    solution = Solution()
    words = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print(ord(" "))
    print("at" + "car")
    print(chr(97))
    for acii in range(ord("a"), ord("z") + 1):
        print(chr(acii))

    # if " ":
    #     print("是空")
    print(solution.findString(words,"car1"))
