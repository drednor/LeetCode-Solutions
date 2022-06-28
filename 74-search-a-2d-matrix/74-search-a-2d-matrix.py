class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            l = 0 
            r = len(i) - 1
            while l<=r:
                mid = l+((r-l)//2)
                if i[mid] == target:
                    return True
                elif target < i[mid]:
                    r = mid - 1
                else:
                    l = mid +1
            
        return False
        