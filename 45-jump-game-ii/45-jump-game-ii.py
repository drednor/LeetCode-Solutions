class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        last_index = len(nums) - 1
        cur_coverage, last_jump_index = 0 ,0 
        res = 0
        for i in range(0,len(nums)):
            cur_coverage = max(cur_coverage, i + nums[i])
            if i == last_jump_index:
                last_jump_index = cur_coverage
                res += 1
                if cur_coverage >= last_index:
                    return res
        return res
            
        
        
        
        
        
        
        
        
        # l = r = 0
        # res = 0
        # while r < len(nums)-1:
        #     farthest = 0
        #     for i in range(l, r+1):
        #         farthest = max(farthest, i + nums[i])
        #     res += 1
        #     l = r+1
        #     r = farthest
        # return res