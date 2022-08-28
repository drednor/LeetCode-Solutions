class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        visit = set()
        def check(r,c):
            temp = [r,c]
            diag = []
            #print("check diag")
            while r < len(mat) and c < len(mat[0]):
                visit.add((r,c))
                diag.append(mat[r][c])
                r += 1
                c += 1
            r , c = temp
            diag.sort(reverse = True)
            while r < len(mat) and c < len(mat[0]) and diag:
                mat[r][c] = diag.pop()
                r+=1
                c+=1
                
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i,j) not in visit:
                    #print("out", [i,j])
                    check(i,j)
                    #print("again out after",[i,j])
        return mat