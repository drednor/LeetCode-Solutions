class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        A = set()
        check = set()
        for i in range(n):
            check.add(i+1)
            if nums[i] in A:
                res.append(nums[i])
            else:
                A.add(nums[i])
        res.append(list(check.difference(A))[0])
        return res
            