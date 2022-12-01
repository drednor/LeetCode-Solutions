class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        check = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        first = 0
        second = 0
        for i in range(len(a)):
            if a[i] in check:
                first += 1
            if b[i] in check:
                second += 1
        return first == second
                
        