class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for i in range(len(matrix)):
            res.extend(matrix[i])
        res.sort()
        return res[k-1]