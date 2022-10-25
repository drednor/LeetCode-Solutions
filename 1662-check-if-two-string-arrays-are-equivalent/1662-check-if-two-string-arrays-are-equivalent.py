class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first = ""
        second = ""
        for word in word1:
            first+=word
        for word in word2:
            second+=word
        return first == second