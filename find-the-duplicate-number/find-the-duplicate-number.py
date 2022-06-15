class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tempmap={}
        for i in nums:
            tempmap[i] = tempmap[i]+1 if i in tempmap else 1
            if tempmap[i] > 1:
                return i
        return -1
        
        #Using Counter 
        # c = Counter(nums)
        # return c.most_common(1)[0][0]