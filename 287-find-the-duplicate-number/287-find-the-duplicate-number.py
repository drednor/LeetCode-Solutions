class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        fast , slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            fast = nums[fast]
            if slow2 == fast:
                return slow2
        
        # # MAKING A HASHMAP AND ADDING VALUE IF VALUE IS ALREADY SEEN
        # tempmap={}
        # for i in nums:
        #     tempmap[i] = tempmap[i]+1 if i in tempmap else 1
        #     if tempmap[i] > 1:
        #         return i
        # return -1
        
        #Using Counter 
        # c = Counter(nums)
        # return c.most_common(1)[0][0]