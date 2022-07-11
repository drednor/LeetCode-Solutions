class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def backtrack(i, sub):
            if i == len(nums):
                result.append(sub)
                return
            backtrack(i+1, sub+[nums[i]])
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1,sub)
            return
        backtrack(0,[])
        return result
        # c = []
        # def dfs(array, sub):
        #     if len(array) == 0:
        #         if Counter(sub) not in c:
        #             c.append(Counter(sub))
        #             result.append(sub)
        #         return
        #     num = array[0]
        #     dfs(array[1:],sub+[num])
        #     dfs(array[1:],sub)
        #     return
        # dfs(nums,[])
        # return result