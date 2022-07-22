class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.houserobber1(nums[1:]), self.houserobber1(nums[:len(nums)-1]))
        
        
        
    def houserobber1(self, nums):
        nums.insert(0,0)
        for i in range(len(nums)):
            if i+3<len(nums):
                nums[i+3] += max(nums[i],nums[i+1])
        return max(nums[-1],nums[-2])
        
        
    
        # if len(nums) == 1:
        #     return nums[0]
        # nums.insert(0,0)
        # numscopy = nums.copy()
        # for i in range(len(nums)):
        #     if i+3 < len(nums)-1:
        #         numscopy[i+3] += max(numscopy[i],numscopy[i+1])
        #     if i+3< len(nums):
        #         nums[i+3] += max(nums[i],nums[i+1])
        # print(numscopy, nums)
        # return max(max(numscopy[-2],numscopy[-3]), max(nums[-1],nums[-2]))
        
        
        # memo = {}
        # def recur(i, sub):
        #     if i in memo:
        #         return memo[i]
        #     if i >= len(nums):
        #         return 0
        #     left = sub[0] + recur(i+2,sub[1:len(sub)-1])
        #     right = recur(i+1,sub[1:])
        #     memo[i] = max(left,right)
        #     return memo[i]
        # return recur(0,nums)