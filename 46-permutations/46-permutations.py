class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(array, sub):
            if len(array) == 0:
                result.append(sub)
                return
            num = array[0]
            for i in range(len(sub)+1):
                dfs(array[1:],sub[:i]+[num]+sub[i:len(sub)])
        dfs(nums, [])
        return result