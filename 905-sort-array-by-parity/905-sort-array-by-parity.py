class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j=0
        for i in range(len(nums)):
            if nums[j]%2 != 1:
                j+=1
                continue
            nums.append(nums[j])
            nums.pop(j)
        return nums
        