class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visit = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i,j) not in visit:
                    if matrix[i][j] == 0:
                        visit.add((i,j))
                        for k in range(len(matrix[i])):
                            #print(i,k)
                            if (i,k) not in visit:
                                if matrix[i][k] == 0:
                                    continue
                                else:
                                    matrix[i][k] = 0
                                    visit.add((i,k))
                        for l in range(len(matrix)):
                            #print(l,j)
                            if (l,j) not in visit:
                                if matrix[l][j] == 0:
                                    continue
                                else:
                                    matrix[l][j] = 0
                                    visit.add((l,j))
