class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums[:]]
            
        for i in range(len(nums)):
            n = nums.pop(0)
            #print(n)
            perms = self.permute(nums)
            #print("returned perms =",perms)
            for perm in perms:
                #print("inside for loop perm = ", perm, n)
                perm.append(n)
                
            result.extend(perms)
            nums.append(n)
            
        return result
        
        # def dfs(array, sub):
        #     if len(array) == 0:
        #         result.append(sub)
        #         return
        #     num = array[0]
        #     for i in range(len(sub)+1):
        #         dfs(array[1:],sub[:i]+[num]+sub[i:len(sub)])
        # dfs(nums, [])
        # return result