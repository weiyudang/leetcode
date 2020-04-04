# coding:utf-8
'''
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
动态规划的问题
i,j
'''
class Solution:
    def FindContinuousSequence(self,tsum):
        i=1
        j=2
        cursum=3
        res=[]
        while j<tsum//2:
            if cursum==tsum:
                res.append(range(i,j+1))
                j+=1
                cursum+=j
            elif cursum<tsum:
                j+=1
                cursum+=j
            else:
                cursum-=i
                i+=1
        return res






if __name__ == '__main__':
    tsum=3
    i=1
    j=2
    cursum=3
    res=[]
    print(tsum//2)
    while i<=tsum//2:
        print(i)
        if cursum==tsum:
            res=range(i,j+1)
            j+=1
            cursum+=j
            print(res)
        elif cursum<tsum:
            j += 1
            cursum+=j
        else:
            cursum-=i
            i+=1
        print(i,j)





