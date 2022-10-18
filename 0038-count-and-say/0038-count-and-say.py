class Solution:
    def countAndSay(self, n: int) -> str:
        
        def recur(k):
            if k == 1:
                return "1"
            sub = recur(k-1)
            res = ""
            i = 0
            while i < len(sub):
                count = 1
                while i+1 < len(sub) and sub[i] == sub[i+1]:
                    count+= 1
                    i+=1
                res += str(count) + sub[i]
                i+=1
            return res
        return recur(n)