class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        result = float("-inf")
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    temp = self.explore(grid, r, c, visited)
                    result = max(temp, result)
        if result == float("-inf"):
            return 0
        return result
    
    def explore(self, grid, r, c, visited):
        count = 0
        if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] != 0 and (r,c) not in visited:
            visited.add((r,c))
            count = 1
            count+=self.explore(grid, r+1, c, visited)
            count+=self.explore(grid, r, c+1, visited)
            count+=self.explore(grid, r, c-1, visited)
            count+=self.explore(grid, r-1, c, visited)
            return count
        return count