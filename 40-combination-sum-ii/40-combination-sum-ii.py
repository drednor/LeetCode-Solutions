class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(i, total, sub):
            if total == target:
                if sub not in result:
                    result.append(sub)
                return
            if i >= len(candidates) or total > target:
                return 
            num = candidates[i]
            backtrack(i+1, total + num, sub +[num])
            while i+1 <len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1,total, sub)
            return 
        backtrack(0,0,[])
        return result