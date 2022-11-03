class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        found = 0
        c = Counter(words)
        visited = set()
        for word in c.keys():
            if word[0] == word[1]:
                #if word not in visited:
                num = c[word]
                if num%2 == 1:
                    found = 2
                res += (num//2 *2)*2
                #visited.add(word)
                continue
            else:
                num = min(c[word],c[word[::-1]])
                res+= 2*num
                #visited.add(word)
                #visited.add(temp)
                
        return res + found