class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 
        for i in nums:
            res = i ^ res
        return res
        
        # result = set()
        # for i in nums:
        #     if i in result:
        #         result.remove(i)
        #     else:
        #         result.add(i)
        # return result.pop()
        
        
        
        #Hashmaps
        # result = {}
        # for i in nums:
        #     result[i] = 1 + result.get(i,0) 
        # return (list(result.keys())[list(result.values()).index(1)])