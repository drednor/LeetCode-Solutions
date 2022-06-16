class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        l , r = 0 , len(nums)-1
        mid = l+r
        if mid % 2 == 1:
            mid = mid//2
            return (nums[mid]+nums[mid+1])/2
        else:
            mid = mid//2
            return nums[mid]
        
        