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
                                
        
        # my Solution - Correct solution but does not work with python language on leetcode
        # if len(nums) == 3:
        #     return sum(nums)
        # nums.sort()
        # res = [[None,None,None],float("inf")]
        # for i , n in enumerate(nums):
        #     l = i +1
        #     r = len(nums)-1
        #     while l < r:
        #         temp = res[1]
        #         threesum = n + nums[l] + nums[r]
        #         res[1] = min(res[1],abs(target-(threesum)))
        #         if temp != res[1]:
        #             res[0] = [i,l,r]
        #         if target - threesum > 0:
        #             l += 1
        #         elif target - threesum < 0:
        #             r -= 1
        #         else:
        #             return target
        # return nums[res[0][0]] + nums[res[0][1]] + nums[res[0][2]]