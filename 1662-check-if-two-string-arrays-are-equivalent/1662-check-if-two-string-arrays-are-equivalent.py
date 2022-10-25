class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        temp = "".join(word1)
        temp2 = "".join(word2)
        return temp == temp2