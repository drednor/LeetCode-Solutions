class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = Counter(nums)
        return c.most_common(1)[0][0]