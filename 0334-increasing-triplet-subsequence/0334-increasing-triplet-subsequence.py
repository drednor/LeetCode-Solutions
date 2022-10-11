class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = []
        for num in nums:
            index = bisect_left(dp, num)
            #print(index,dp)
            if index<len(dp):
                dp[index] = num
            else:
                dp.append(num)
            if len(dp)> 2:
                return True
        return False
                