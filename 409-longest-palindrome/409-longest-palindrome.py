class Solution:
    def longestPalindrome(self, s: str) -> int:
        temp = {}
        result = 0
        for char in s:
            temp[char] = 1+temp[char] if char in temp else 1
        for char, val in temp.items():
            result += int(val/2) * 2
            if result %2 == 0 and val % 2 == 1:
                result += 1
        return result