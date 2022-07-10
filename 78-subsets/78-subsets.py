class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def subset(nums,sub):
            if len(nums) == 0:
                result.append(sub)
                return
            first = nums[0]
            subset(nums[1:],sub + [first])
            subset(nums[1:],sub)
            return
        subset(nums,[])
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # result = []
        # temp = []
        # def dfs(i):
        #     if i >= len(nums):
        #         result.append(temp.copy())
        #         return 
        #     temp.append(nums[i])
        #     dfs(i+1)
        #     temp.pop()
        #     dfs(i+1)
        # dfs(0)
        # return result