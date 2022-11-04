class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s)-1
        check = {'a', 'e', 'i', 'o','u','A', 'E', 'I', 'O','U'}
        while i < j:
            #print(s[i], s[j])
            if s[i] in check and s[j] in check:
                # s = s[:i] + s[j] + s[i + 1:]
                # s = s[:j] + s[i] + s[j + 1:]
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
                continue
            if s[i] not in check:
                i+=1
            if s[j] not in check:
                j-=1
        return "".join(s)
                