class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if list(sorted(s)) == list(sorted(t)):
            return True
        else:
            return False
        