class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = set()
        
        def dfs(r, c):
            if 0<=r<rows and 0<=c<cols and (r, c) not in visited and board[r][c] != "X":
                visited.add((r,c))
                dfs(r+1,c)
                dfs(r,c+1)
                dfs(r-1,c)
                dfs(r,c-1)
            return 
        
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)
        
        for c in range(cols):
            dfs(0 , c)
            dfs(rows-1, c)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and board[r][c] != "X":
                    board[r][c] = "X"
        