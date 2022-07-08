class Solution:
    def numberOfSteps(self, num: int) -> int:
        # count = 0
        # while num!=0:
        #     count += 1
        #     if num%2 == 0:
        #         num //= 2
        #     else:
        #         num -=1
        # return count
        count = [0]
        def helper(num):
            if num == 0 :
                return count[0]
            count[0] += 1
            if num % 2 == 0:
                return helper(num//2)
            return helper(num-1)
        return helper(num)