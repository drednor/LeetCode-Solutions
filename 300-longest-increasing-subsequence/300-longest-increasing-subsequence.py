class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        table = []
        for num in nums:
            if len(table) == 0 or table[-1] < num:
                table.append(num)
            else:
                idx = bisect.bisect_left(table, num)
                table[idx] = num
        return len(table)
#         table = [1] * len(nums)
#         for i in range(len(nums)-1,-1,-1):
#             for j in range(i+1, len(nums)):
#                 if nums[j] > nums[i]:
#                     table[i] = max(table[i], 1 + table[j])
#         return max(table)