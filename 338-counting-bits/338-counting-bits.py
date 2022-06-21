class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] *(n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            result[i] = 1 + result[i - offset]
        return result
        
        
        # Just Count the number of ones
        # foreach value of i and append
        # it to the result time complexity - O(nlogn) 
        # result = []
        # for i in range(n+1):
        #     res = 0
        #     while i:
        #         i &= i-1
        #         res +=1
        #     result.append(res) 
        # return result 
        