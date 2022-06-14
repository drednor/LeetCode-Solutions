class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        for i in range(len(nums)):
            if nums[i] == target:
                result[0] = i
                break
        else:
            return result
        for i in range(len(nums)-1, -1,-1):
            if nums[i] == target:
                result[1] = i
                break
        return result
        # l , r = 0 , len(nums)
        # while l<=r:
        #     mid = (l+r)//2