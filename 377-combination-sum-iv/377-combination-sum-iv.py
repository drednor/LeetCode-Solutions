class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # table = [0] * (target+1)
        # table[0] = 1
        # for i in range(len(table)):
        #     if table[i] == 0:
        #         for num in nums:
        #             temp = i - num
        #             if temp>=0:
        #                 table[i] += table[temp]
        # #print(table)
        # return table[target]
    
        table = [0] * (target +1)
        table[0] = 1
        for i in range(len(table)):
            if table[i] != 0:
                for num in nums:
                    temp = i + num
                    if temp < len(table):
                        table[temp] += table[i]
        return table[target]
                
        # memo = {}
        # def recur(total):
        #     key = total
        #     if key in memo:
        #         return memo[key]
        #     if total < 0:
        #         return 0
        #     count = 0
        #     for num in nums:
        #         if total > num:
        #             count += recur(total - num)
        #         if total == num:
        #             count += 1
        #     memo[key] = count
        #     return memo[key]
        # return recur(target)
            