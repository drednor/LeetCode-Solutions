class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        og = x
        num = 0
        while x:
            num = num * 10 + x%10
            x = x//10
        return og == num
        
        
        
        # if x < 0:
        #     return False
        # res = []
        # while x:
        #     temp = x%10
        #     x = x//10
        #     res.append(temp)
        # i = 0
        # j = len(res)-1
        # while i<j:
        #     if res[i] != res[j]:
        #         return False
        #     i+=1
        #     j-=1
        # return True