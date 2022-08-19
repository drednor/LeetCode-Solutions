class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        table = [[0]*len(nums) for _ in range(len(nums))]
        
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+2,len(nums)):
                table[i][j] = max(nums[i]*nums[j]*nums[k] + table[i][k] + table[k][j] for k in range(i+1,j))
        return table[0][len(nums)-1]
        
        # nums = [1] + nums + [1]
        # memo = {}
        # def recur(l,r):
        #     key = (l,r)
        #     if l > r:
        #         return 0
        #     if key in memo:
        #         return memo[key]
        #     memo[key] = 0
        #     for i in range(l, r+1):
        #         coin = nums[l-1] *nums[i]*nums[r+1]
        #         coin += recur(l,i-1) + recur(i+1,r)
        #         #print(coin, l , r, i)
        #         memo[key] = max(memo[key],coin)
        #     return memo[key]
        # return recur(1,len(nums)-2)
        
        
        # memo ={}
        # something = [float("-inf")]
        # def recur(i,sub,res):
        #     key = (tuple(sub),res)
        #     if key in memo:
        #         return memo[key]
        #     if len(sub) == 1:
        #         return res + sub[0]
        #     temp = 0
        #     for num in sub:
        #         if i - 1 < 0 and i+1>=len(sub):
        #             temp = sub[i] 
        #         elif i - 1< 0:
        #             temp = sub[i] * sub[i+1]
        #         elif i+1 >= len(sub):
        #             temp = sub[i-1] * sub[i]
        #         else:
        #             temp = sub[i-1] * sub[i] * sub[i+1]    
        #         result = recur(0,sub[:i]+sub[i+1:],res + temp)
        #         # print(result)
        #         if result > something[0]:
        #             something[0] = result
        #         i+=1
        #     memo[key] = something[0]
        #     return something[0]
        # return recur(0,nums,0)
                