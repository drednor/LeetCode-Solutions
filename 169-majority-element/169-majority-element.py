class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memo = {}
        for num in nums:
            memo[num] = 1 + memo[num] if num in memo else 1
        temp = [None,float("-inf")]
        for key, val in memo.items():
            if val > temp[1]:
                temp = [key, val]
        return temp[0]