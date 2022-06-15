class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l , r = 0 , len(letters)-1
        if target<letters[l] or target >= letters[r]: 
            return letters[l]
        while l<=r:
            mid = (l+r)//2
            if target<letters[mid]:
                r = mid-1
            else:
                l = mid +1
        return letters[l]