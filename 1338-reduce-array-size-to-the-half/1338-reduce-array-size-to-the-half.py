class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        memo = Counter(arr).most_common()
        # print(memo)
        total = len(arr)
        # print(total)
        temp = 0
        res = float("inf")
        for key, val in memo:
            total -= val
            temp += 1
            # print(key, val, temp, total)
            if total<= len(arr)//2:
                break
        return temp