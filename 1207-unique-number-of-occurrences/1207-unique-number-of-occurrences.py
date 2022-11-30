class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        check = set()
        for v in c.values():
            if v in check:
                return False
            check.add(v)
        return True