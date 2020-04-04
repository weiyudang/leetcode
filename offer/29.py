# coding:utf-8
'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。
'''


class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return
        if len(numbers) == 1:
            return numbers[0]

        self.min_number = '99999999'
        self.dfs(numbers, '')
        return self.min_number

    def dfs(self, numbers, path):
        if not numbers:
            if self.min_number > path:
                self.min_number = path

        for i in range(len(numbers)):
            l1 = path + str(numbers[i])
            # print(l1)
            self.dfs(numbers[:i] + numbers[i + 1:], l1)

if __name__ == '__main__':
    arr = [3,32,321]
    solution=Solution()
    print(solution.PrintMinNumber(arr))
