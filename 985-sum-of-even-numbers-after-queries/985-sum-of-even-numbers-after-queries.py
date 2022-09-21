class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        temp = 0
        for num in nums:
            if num%2 == 0:
                temp+= num
        start_sum = temp
        for val, idx in queries:
            if nums[idx] % 2 == 1:
                before_odd = True
            else:
                temp = nums[idx]
                before_odd = False
            nums[idx] += val
            if nums[idx]%2 == 0 and before_odd:
                start_sum += nums[idx]
            elif nums[idx]%2 == 1 and before_odd:
                start_sum = start_sum
            elif nums[idx]%2 == 0 and not before_odd:
                start_sum += val
            elif nums[idx]%2 == 1 and not before_odd:
                start_sum -= temp
            res.append(start_sum)
        return res
        