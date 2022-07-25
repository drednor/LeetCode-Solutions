class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total//2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            dpcopy = dp.copy()
            for val in dp:
                dpcopy.add(val + nums[i])
            dp = dpcopy
        return True if target in dp else False