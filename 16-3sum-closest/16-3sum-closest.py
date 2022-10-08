class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        cur = sum(nums[:3])
        if cur >= target:
            return cur
        
        cur = sum(nums[-3:])
        if cur < target:
            return cur
        for i in range(len(nums)-2):
            l = i +1
            r = len(nums)-1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if abs(target-threesum) < abs(res-target):
                    res = threesum
                if threesum < target:
                    l += 1
                else:
                    r -= 1
        return res
                                