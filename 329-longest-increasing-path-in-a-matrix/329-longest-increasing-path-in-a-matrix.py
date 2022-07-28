class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        visited = {}
        self.res = -1
        def dfs(r,c, prev):
            if 0<=r<rows and 0<=c<cols and matrix[r][c] > prev:
                if (r,c) in visited:
                    return visited[(r,c)]
                count = 1
                count = max(count, 1 + dfs(r+1,c,matrix[r][c]))
                count = max(count, 1 + dfs(r,c+1,matrix[r][c]))
                count = max(count, 1 + dfs(r-1,c,matrix[r][c]))
                count = max(count, 1 + dfs(r,c-1,matrix[r][c]))
                visited[(r,c)] = count
                self.res = max(count, self.res)
                return count
            return 0
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,-1)
        return self.res
                            
                            