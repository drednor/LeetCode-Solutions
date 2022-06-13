def checkallvalues(arr,value, start=0, end =0):
        if len(arr[start:end]) == 0:
            return False
        if start == 0:
            for i in range(len(arr[start:end])-1,-1,-1):
                if arr[i] >= value:
                    return False
                value = arr[i]
            return True
        else:
            for i in arr[start:end]:
                if i >= value:
                    return False
                value = i
            return True

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        g = sorted(arr)
        value = g[-1]
        max_value_index = arr.index(value)   
        l = checkallvalues(arr,value, 0, max_value_index)
        r = checkallvalues(arr,value, max_value_index+1, len(arr)+1)
        if l and r:
            return True
        else:
            return False
        
        
        
    
            
        