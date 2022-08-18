class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1,numRows+1):
            temp = [1] * i
            res.append(temp)
        for i in range(len(res)):
            if i > 1:
                for j in range(1,len(res[i])-1):
                    if j-1>=0:
                        res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res