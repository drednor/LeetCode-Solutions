class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        for key, val in r.items():
            if key in m and r[key] <= m[key]:
                continue
            else:
                return False
        return True