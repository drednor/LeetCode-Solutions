class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        size = 0
        res = []
        end = 0
        print(last)
        for i in range(len(s)):
            size += 1
            end = max(end, last[s[i]])
            if i == end:
                res.append(size)
                size = 0
        return res
            
        
        
        # res = []
        # c = Counter(s)
        # visit = set()
        # temp = 0
        # for i in range(len(s)):
        #     visit.add(s[i])
        #     temp += 1
        #     c[s[i]] -= 1
        #     if c[s[i]] == 0:
        #         visit.remove(s[i])
        #     if len(visit) == 0:
        #         res.append(temp)
        #         temp = 0
        # return res
        
        