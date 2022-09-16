class Solution:
    def maximumScore(self, nums: List[int], mul: List[int]) -> int:
        # @lru_cache(2000)
        # def recur(l, i):
        #     if i == len(multipliers):
        #         return 0
        #     return max(nums[l] * multipliers[i] + recur(l+1, i+1), nums[n-i+l] * multipliers[i] + recur(l, i+1))
        # n = len(nums)-1
        # res = recur(0,0)
        # recur.cache_clear()
        # return res
        dp = [0] * (len(mul) + 1)
        for m in range(len(mul) - 1, -1, -1):
            pd = [0] * (m + 1)
            for l in range(m, -1, -1):
                pd[l] = max(dp[l + 1] + mul[m] * nums[l], 
                            dp[l] + mul[m] * nums[~(m - l)])
            dp = pd
        return dp[0]
            
            
            
            
            # if startnum * startmul > startnum * endmul and startnum * startmul > endnum * endmul and startnum * startmul > endnum * startmul:
            #     total += startnum * startmul
            #     nums.pop(0)
            #     multipliers.pop(0)
            # elif startnum * endmul > startnum * startmul and startnum * endmul > endnum * endmul and startnum * endmul > endnum * startmul:
            #     total += startnum * endmul
            #     nums.pop(0)
            #     multipliers.pop(-1)
            # elif endnum * startmul > startnum * startmul and endnum * startmul > endnum * endmul and endnum * startmul > endmul * startnum:
            #     total += endnum * startmul
            #     nums.pop(-1)
            #     multipliers.pop(0)
            # else:
            #     total += endnum * endmul
            #     nums.pop(-1)
            #     multipliers.pop(-1)
        #return total