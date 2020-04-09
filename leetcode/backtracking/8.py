#coding:utf-8
'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]

        self.dfs(nums,[],res)
        return  res

    def dfs(self,nums,path,res):
        if not nums:
            res.append(path)
            return
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)




if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.subsets(nums))
