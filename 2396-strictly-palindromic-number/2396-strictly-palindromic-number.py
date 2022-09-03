class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for b in range(2,n-1):
            temp = n
            s = ""
            while temp:
                s += str(temp%b)
                temp //= b
            if s[::-1] != s:
                return False
        return True