class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # c = Counter(nums).most_common()
        # return c[0][0]
        res, count = 0 , 0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if res == num else -1)
        return res
        
        
        # memo = {}
        # temp = [None, float("-inf")]
        # for num in nums:
        #     memo[num] = 1 + memo[num] if num in memo else 1
        #     val = memo[num]
        #     if val > temp[1]:
        #         temp = [num, val]
        # return temp[0]
        