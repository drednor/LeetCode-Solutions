class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix)-1
        while l < r:
            for i in range(r-l):
                top , bot = l ,r
                topleft = matrix[top][l+i]
                matrix[top][l+i] = matrix[bot-i][l]
                matrix[bot-i][l] = matrix[bot][r-i]
                matrix[bot][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topleft
            l+=1
            r-=1
        

        
        # l , r = 0, len(matrix)-1
        # while l < r:
        #     for i in range(r-l):
        #         top , bottom = l , r
        #         topleft = matrix[top][l+i]
        #         matrix[top][l+i] = matrix[bottom-i][l]
        #         matrix[bottom-i][l] = matrix[bottom][r-i]
        #         matrix[bottom][r-i] = matrix[top+i][r]
        #         matrix[top+i][r] = topleft
        #     l+=1
        #     r-=1