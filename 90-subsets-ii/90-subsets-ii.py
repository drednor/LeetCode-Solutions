class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        c = []
        def dfs(array, sub):
            if len(array) == 0:
                if Counter(sub) not in c:
                    c.append(Counter(sub))
                    result.append(sub)
                return
            num = array[0]
            dfs(array[1:],sub+[num])
            dfs(array[1:],sub)
            return
        dfs(nums,[])
        return result