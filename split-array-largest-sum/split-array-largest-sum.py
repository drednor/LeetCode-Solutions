class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def splitarray(largest):
            subarray = 1;
            totalsum = 0
            for n in nums:
                totalsum += n
                if totalsum > largest:
                    subarray+=1
                    totalsum =n
            return subarray<=m
        
        l = max(nums)
        r = sum(nums)
        res = r
        while l<=r:
            mid = (l+r)//2
            if splitarray(mid):
                res = mid
                r = mid -1
            else:
                l = mid + 1
        return res