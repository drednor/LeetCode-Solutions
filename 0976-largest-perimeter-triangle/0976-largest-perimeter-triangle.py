class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        for i in range(n):
            if i+2 < n and nums[i] < nums[i+2] + nums[i+1]:
                return nums[i] + nums[i+2] + nums[i+1]
        return 0
                