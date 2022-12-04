class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        res = [float("inf"),float("inf")]
        start = 0
        for i, num in enumerate(nums):
            start += num
            total -= num
            if i != n-1:
                temp = abs(start//(i+1) - total//(n-i-1))
            else:
                temp = abs(start//(i+1))
            if temp == res[1]:
                continue
            if temp < res[1]:
                res[1] = temp
                res[0] = i
        return res[0]
            
        