#coding:utf-8

'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
思路：
双指针法
注意控制 前后指针 i<j  双指针法可以解决位置调换
low  high

从先开始遍历，直至找到一个偶数的数字，标记
从后往前遍历，找到一个奇数，然后两个坐标位置交换

暴力法：
直接进行循环遍历一遍，奇数的放到一个list 偶数放到一个容器然后再拼接
'''

class Solution:
    def reOrderArray(self, array):
        if not array:
            return

        res1=[]
        res2=[]

        for i in array:
            if i&1==1:
                res1.append(i)
            else:
                res2.append(i)
        return res1+res2
    def reOrderArray2(self,array):

        if not array:
            return

        i=0
        j=len(array)-1

        while i<j:
            while i<j and self.judge(array[i]):
                i+=1
            while i<j and not self.judge(array[j]):
                j-=1
            array[i],array[j]=array[j],array[i]
        return array
    def judge(self,n):
        # return n&1==1
        return n%4==0

if __name__ == '__main__':
    array=[1,2,3,4,5,6,7,8,9]
    solution=Solution()
    print(solution.reOrderArray2(array))
    print(3&1)