class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax , curMin = 1, 1
        for num in nums:
            if num == 0:
                curMax , curMin = 1, 1
            temp = num * curMax
            curMax = max(temp, num*curMin,num)
            curMin = min(temp, num*curMin, num)
            res = max(curMax, res)
        return res
            
        
        