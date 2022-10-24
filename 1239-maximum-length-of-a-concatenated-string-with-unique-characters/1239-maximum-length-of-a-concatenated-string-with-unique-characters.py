class Solution:
    def maxLength(self, arr: List[str]) -> int:
        check = set()
        
        def overlap(check, s):
            temp = set()
            for char in s:
                if char in check or char in temp:
                    return True
                temp.add(char)
            return False
        
        def backtrack(i):
            if i == len(arr):
                return len(check)
            res = 0
            if not overlap(check, arr[i]):
                for char in arr[i]:
                    check.add(char)
                res = backtrack(i+1)
                for char in arr[i]:
                    check.remove(char)
            return max(res,backtrack(i+1))
        return backtrack(0)