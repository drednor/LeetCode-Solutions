class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        table = [0] * (target+1)
        table[0] = 1
        for i in range(len(table)):
            if table[i] == 0:
                for num in nums:
                    temp = i - num
                    if temp>=0:
                        table[i] += table[temp]
        #print(table)
        return table[target]
        
        
        # memo = {}
        # self.res = 0
        # def recur(total):
        #     key = total
        #     if key in memo:
        #         return memo[key]
        #     if total == 0:
        #         #print(sub)
        #         return 1
        #     if total < 0:
        #         return 0
        #     for num in nums:
        #         rem = total - num
        #         memo[key] = recur(rem, sub + tuple([num]))
        #         if memo[key]:
        #             self.res += 1
        #     return memo[key]
        # recur(target,())
        # return self.res
            