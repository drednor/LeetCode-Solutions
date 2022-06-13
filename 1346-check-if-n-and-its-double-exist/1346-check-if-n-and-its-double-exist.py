
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        x = collections.Counter(arr)
        
        if (x[0]>1):
            return True
        for i in arr:
            if x[2*i] and i!=0:
                return True 
        return False
        