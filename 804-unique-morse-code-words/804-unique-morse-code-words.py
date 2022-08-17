class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        temp2 = ""
        for word in words:
            for char in word:
                temp = ord(char) - ord("a")
                temp2 += morse[temp]
            if temp2 not in res:
                res.append(temp2)
            temp2 = ""
        return len(res)