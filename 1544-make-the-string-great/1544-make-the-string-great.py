class Solution:
    def makeGood(self, s: str) -> str:  
        res = s
        temp = ""
        
        def msg(word):
            ans = ""
            i = 0
            while i < len(word):
                char = word[i]
                if char.isupper():
                    if i+1<len(word) and char.lower() == word[i+1]:
                        i+=2
                        continue

                if i+1<len(word) and char.upper() == word[i+1] and char.islower():
                    i+=2
                    continue
                ans += char
                i+=1
            return ans
        
        while True:
            temp = res
            res = msg(temp)
            if temp == res:
                break
        return res
        