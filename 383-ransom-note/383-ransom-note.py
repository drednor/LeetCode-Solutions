class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = {}
        m = {}
        for char in ransomNote:
            r[char] = 1 + r[char] if char in r else 1
        for char in magazine:
            m[char] = 1 + m[char] if char in m else 1
        for key, val in r.items():
            if key in m and r[key] <= m[key]:
                continue
            else:
                return False
        return True