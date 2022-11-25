class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        stack = [-1]
        arr.append(0)
        res = 0
        for i in range(len(arr)):
            while arr[i] < arr[stack[-1]]:
                idx = stack.pop()
                res += arr[idx] * (i -idx) * (idx - stack[-1])
            stack.append(i)
        return res % mod