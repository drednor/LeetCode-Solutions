class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        goal = len(nums) -1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0