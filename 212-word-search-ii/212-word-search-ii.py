class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addword(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addword(word)
        
        row = len(board)
        col = len(board[0])    
        visited , result = set() , set()
        
        def dfs(r, c, node, word):
            if (r<0 or c<0 or r == row or c == col or (r,c) in visited or board[r][c] not in node.children):
                return
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:
                result.add(word)
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)
            visited.remove((r,c))
            
        for r in range(row):
            for c in range(col):
                dfs(r,c,root,"")
        return list(result)                