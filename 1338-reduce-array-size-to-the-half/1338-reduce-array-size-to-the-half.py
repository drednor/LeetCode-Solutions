class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        memo = {}
        for num in arr:
            memo[num] = 1+ memo[num] if num in memo else 1
        temp = []
        for key, val in memo.items():
            temp.append(val)
        temp.sort(reverse=True)
        res = 0
        total = len(arr)
        for num in temp:
            total -= num
            res+=1
            if total <= (len(arr)//2):
                break
        return res
        # memo = Counter(arr).most_common()
        # # print(memo)
        # total = len(arr)
        # # print(total)
        # temp = 0
        # res = float("inf")
        # for key, val in memo:
        #     total -= val
        #     temp += 1
        #     # print(key, val, temp, total)
        #     if total<= len(arr)//2:
        #         break
        # return temp