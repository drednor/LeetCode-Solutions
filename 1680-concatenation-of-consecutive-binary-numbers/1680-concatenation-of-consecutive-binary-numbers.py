class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = ""
        mod = 10**9 + 7
        for i in range(1,n+1):
            s += bin(i)[2:]
        return int(s,2)%mod
            
            
            
            
        # for i in range(len(s)):
        #     res += (int(s[i])*(2**(len(s)-1-i)))
        # return res%mod
        