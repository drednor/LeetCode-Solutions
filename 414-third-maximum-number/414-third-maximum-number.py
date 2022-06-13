class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        c = Counter(nums)
        c= sorted(c.items(), reverse=True)
        if len(c)<=2:
            return max(nums)
        else:
            return c[2][0]
                