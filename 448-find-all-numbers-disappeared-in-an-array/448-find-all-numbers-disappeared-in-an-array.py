class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # j = 1
        # result = []
        # for i in range(len(nums)):
        #     if j in nums:
        #         j+=1
        #         continue
        #     else:
        #         result.append(j)
        #         j+=1
        # return result
        y = sorted(nums)
        y = set(y)
        return [x for x in range(1,len(nums)+1) if x not in y]
#         x = set(x)
#         result = list(x.difference(y))
#         return result
                
            
            
        