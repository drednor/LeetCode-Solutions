class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        q = deque()
        for i, char in enumerate(dom):
            if char != ".":
                q.append((i, char))
        
        while q:
            i, char = q.popleft()
            #print(q)
            if char == "L":
                if i > 0 and dom[i-1] == ".":
                    q.append((i-1,"L"))
                    dom[i-1] = "L"
                
            if char == "R":
                if i + 1< len(dom) and dom[i+1] == ".":
                    if i+2 < len(dom) and dom[i+2] == "L":
                        q.popleft()
                    else:
                        q.append((i+1,"R"))
                        dom[i+1] = "R"
        return "".join(dom)