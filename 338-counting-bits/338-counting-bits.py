class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] *(n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            result[i] = 1 + result[i - offset]
        return result
    
        # Sample Input - n = 8
        # Iteration 1 ---> 0b0001 result[1] = 1 + result[1 - 1] | Result right now = [0, 1, 0, 0, 0, 0, 0, 0, 0]
        # Iteration 2 ---> 0b0010 result[2] = 1 + result[2 - 2] | Result right now = [0, 1, 1, 0, 0, 0, 0, 0, 0]
        # Iteration 3 ---> 0b0011 result[3] = 1 + result[3 - 2] | Result right now = [0, 1, 1, 2, 0, 0, 0, 0, 0]
        # Iteration 4 ---> 0b0100 result[4] = 1 + result[4 - 4] | Result right now = [0, 1, 1, 2, 1, 0, 0, 0, 0]
        # Iteration 5 ---> 0b0101 result[5] = 1 + result[5 - 4] | Result right now = [0, 1, 1, 2, 1, 2, 0, 0, 0]
        # Iteration 6 ---> 0b0110 result[6] = 1 + result[6 - 4] | Result right now = [0, 1, 1, 2, 1, 2, 2, 0, 0]
        # Iteration 7 ---> 0b0111 result[7] = 1 + result[7 - 4] | Result right now = [0, 1, 1, 2, 1, 2, 2, 3, 0]
        # Iteration 8 ---> 0b1000 result[8] = 1 + result[8 - 8] | Result right now = [0, 1, 1, 2, 1, 2, 2, 3, 1]
        
        
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
        