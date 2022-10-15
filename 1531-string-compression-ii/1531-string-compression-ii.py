class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(start, last, last_count, left):
            if left<0:
                return float("inf")
            if start>=len(s):
                return 0
            if s[start] == last:
                incr = 1 if last_count == 1 or last_count==9 or last_count == 99 else 0
                return incr + dp(start+1,last,last_count+1, left)
            else:
                keep_counter = 1 + dp(start+1,s[start],1,left)
                del_counter = dp(start+1,last,last_count,left-1)
                return min(keep_counter,del_counter)
        return dp(0,"",0,k)
                
        
        
        
        
        
        # c = Counter(s)
        # check = sorted(c.items(), key=lambda kv:
        #          (kv[1], kv[0]))
        # res = ""
        # print(check)
        # for i in range(len(check)):
        #     if k == 0:
        #         for j in range(i,len(check)):
        #             char, count = check[j]
        #             if count > 1:
        #                 res += char + str(count)
        #             elif count == 1:
        #                 res += char
        #         print(res)
        #         return len(res)
        #     char, count = check[i]
        #     while count and k:
        #         count -= 1
        #         k-=1
        #         if k == 0 and count > 0:
        #             if count > 1:
        #                 res += char + str(count)
        #             elif count == 1:
        #                 res += char 
        # return len(res)
                