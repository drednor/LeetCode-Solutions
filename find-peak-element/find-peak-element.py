class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 0:
            return None
        l , r = 0 , len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if all(nums[mid]>x for x in sorted(nums[:mid])):
                l = mid+1
            else:
                r = mid-1
        return l-1
        