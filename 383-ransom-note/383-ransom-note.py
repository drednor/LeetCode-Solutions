class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        memo = {}
        for char in magazine:
            memo[char] = 1 + memo[char] if char in memo else 1
        
        for char in ransomNote:
            if char in memo and memo[char] > 0:
                memo[char] -= 1
            else:
                return False
        return True