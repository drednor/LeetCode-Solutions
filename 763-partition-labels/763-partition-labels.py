class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        c = Counter(s)
        visit = set()
        temp = 0
        for i in range(len(s)):
            visit.add(s[i])
            temp += 1
            c[s[i]] -= 1
            if c[s[i]] == 0:
                visit.remove(s[i])
            if len(visit) == 0:
                res.append(temp)
                temp = 0
        return res