class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if word1 == word2:
            return True
        if set(word1) != set(word2):
            return False
        c = Counter(word1)
        d = Counter(word2)
        i = 0
        for k, v in c.items():
            if k in d:
                i+=1
        if i <= 1:
            return False
        idx = set()
        x = c.values()
        y = d.values()
        temp = Counter(x)
        temp1 = Counter(y)
        for k,v in temp.items():
            if temp[k] != temp1[k]:
                return False
        return True