class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarySearch(sub, val):
            lo, hi = 0, len(sub)-1
            while(lo <= hi):
                mid = lo + (hi - lo)//2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo
        
        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)
        
#         def binarysearch(num, sub):
#             l , r = 0, len(sub)-1
#             while l<=r:
#                 mid = (l+r)//2
#                 if sub[mid] < num:
#                     l = mid+1
#                 elif num > sub[mid]:
#                     r = mid -1
#                 else:
#                     return mid
#             return l
#         table = []
#         for num in nums:
#             pos = binarysearch(num, table)
#             if pos == len(table):
#                 table.append(num)
#             else:
#                 table[pos] = num
#         return len(table)
        
        
        
        
        
        # table = []
        # for num in nums:
        #     if len(table) == 0 or table[-1] < num:
        #         table.append(num)
        #     else:
        #         idx = bisect.bisect_left(table, num)
        #         table[idx] = num
        # return len(table)
#         table = [1] * len(nums)
#         for i in range(len(nums)-1,-1,-1):
#             for j in range(i+1, len(nums)):
#                 if nums[j] > nums[i]:
#                     table[i] = max(table[i], 1 + table[j])
#         return max(table)