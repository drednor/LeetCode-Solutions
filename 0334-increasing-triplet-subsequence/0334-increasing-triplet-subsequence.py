class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        low = mid = float("inf")
        for num in nums:
            if num <= low:
                low = num
            elif num <= mid:
                mid = num
            else:
                return True
        return False
                