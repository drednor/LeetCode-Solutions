class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                #print(total, i , n)
                return True
        return False
        
        # n = len(nums)
        # memo = {}
        # for i in range(n):
        #     total = nums[i]
        #     if i+1 < n and nums[i] == 0 and nums[i+1] == 0:
        #         return True
        #     for j in range(i+1,n):
        #         if i != j:
        #             total += nums[j]
        #             if total%k == 0:
        #                 return True
        # return False