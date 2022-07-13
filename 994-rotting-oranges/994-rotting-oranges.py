class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        fresh = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r , c = q.popleft()
                for dr , dc in directions:
                    row = dr + r
                    col = dc + c
                    if 0<=row<rows and 0<=col<cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))
            time+=1
                
        return time if fresh == 0 else -1