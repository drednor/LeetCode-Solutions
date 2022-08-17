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
        # result = 1
        # print(res)
        # for i in range(len(res)):
        #     if i+1 < len(res):
        #         if res[i] != res[i+1]:
        #             result+=1
        # return result
            