class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # c = Counter(nums).most_common()
        # return c[0][0]
        memo = {}
        temp = [None, float("-inf")]
        for num in nums:
            memo[num] = 1 + memo[num] if num in memo else 1
            val = memo[num]
            if val > temp[1]:
                temp = [num, val]
        return temp[0]
        # temp = [None,float("-inf")]
        # for key, val in memo.items():
        #     if val > temp[1]:
        #         temp = [key, val]
        # return temp[0]