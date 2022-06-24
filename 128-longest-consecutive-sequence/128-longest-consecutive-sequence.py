class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tempset = set(nums)
        longest = 0
        
        for i in nums:
            if (i-1) not in tempset:
                length = 0
                while (i+length) in tempset:
                    length+=1
                longest = max(length, longest)
        return longest