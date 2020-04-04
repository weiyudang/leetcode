# coding:utf-8
'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
思路1：循环
思路2：n=k*10^c  c
'''


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count=0
        for i in range(1,n+1):
            j=i
            while j:
                if j%10==1:
                    count+=1
                j=j//10
        return count



if __name__ == '__main__':
    n = 13
