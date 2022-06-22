class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            result[i] = 1+result[i] if i in result else 1
            
        for n, c in result.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0 ,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        