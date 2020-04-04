#coding:utf-8
'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
n=2 10->1
n=3 11->2
n=9 1001->2

思路1:移位 >> 依次与&0x1直至数据为0
思路： n&(n-1) 每个数字n 与n-1 进行与运算可以消除最后一个1   1001—1000 0111
'''


class Solution:
    def NumberOf1(self,n):
        count=0
        if n<0:
            n = n & 0xffffffff
        while n:
            n=n&(n-1)
            count+=1
        return count




if __name__ == '__main__':
    n=-2
    count=0
    if n<0:
        n=n&0xffffffff
    while n:
        if n&1==1:
            count+=1
        n=n>>1

    print(count)




