class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = strs[0]
        res= ""
        for word in strs:
            for i in range(len(temp)):
                if i < len(word) and temp[i] == word[i]:
                    res += word[i]
                else:
                    break
            temp = res
            res = ""
        return temp