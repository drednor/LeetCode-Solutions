class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        c = sorted(c.items(), key = lambda x:x[1], reverse = True)
        res = ""
        for char,count in c:
            res += char*count
        return res