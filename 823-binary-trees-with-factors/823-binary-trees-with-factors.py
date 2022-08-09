class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        memo = defaultdict(int)
        for root in arr:
            temp = 1
            for child in arr:
                if child > root: break
                temp += (memo[child]*memo[root/child])
            memo[root] = temp
        return sum(memo.values())%(10**9+7)
            