class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        res = float("-inf")
        row = len(matrix)
        col = len(matrix[0])
        for l in range(col):
            total = [0] * row
            for r in range(l, col):
                for i in range(row):
                    total[i] += matrix[i][r]
                #print(total)
                #res = max(total[i],res)
                arr =[0, math.inf]
                temp = 0
                for num in total:
                    temp += num
                    idx = bisect.bisect_left(arr, temp - k)
                    res = max(res, temp - arr[idx])
                    if res == k:
                        return k
                    bisect.insort(arr, temp)
        return res