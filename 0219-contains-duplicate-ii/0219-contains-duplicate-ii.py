class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in memo:
                memo[nums[i]] = i
                continue
            if abs(memo[nums[i]] - i) <= k:
                return True
            else:
                memo[nums[i]] = i
        return False