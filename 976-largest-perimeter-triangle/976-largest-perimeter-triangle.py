class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        x = sorted(nums, reverse=True)
        for i in range(len(x)-2):
            if x[i] < x[i+1] +x[i+2]:
                return x[i]+x[i+1]+x[i+2]
        return 0
        