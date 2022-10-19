class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []
        memo = defaultdict(int)
        for word in words:
            memo[word] += 1
        memo2 = {}
        for key, val in memo.items():
            if val not in memo2:
                memo2[val] = []
            memo2[val].append(key)
        temp = 0
        for key in sorted(memo2.keys(),reverse= True):
            for val in sorted(memo2[key]):
                res.append(val)
                temp += 1
                if temp == k:
                    return res
        
            
        
        