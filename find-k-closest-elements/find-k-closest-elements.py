class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l , r = 0 , len(arr)-k
        while l<r:
            mid = (l+r)//2
            if x-arr[mid] > arr[mid+k] - x:
                l = mid+1
            else:
                r = mid
        return arr[l:l+k]
        # if len(arr) == k:
        #     return arr
        # l, r = 0, len(arr)-1
        # val = arr[0]
        # idx = 0
        # while l<=r:
        #     mid = (l+r)//2
        #     curdiff, resdiff = abs(arr[mid]-x), abs(val - x)
        #     if curdiff<resdiff or curdiff == (resdiff and arr[mid]<val):
        #         val , idx = arr[mid], mid
        #     if x > arr[mid]:
        #         l = mid+1
        #     elif x < arr[mid]:
        #         r = mid-1
        #     else:
        #         break
        # l = r= idx
        # for i in range(k-1):
        #     if l == 0:
        #         r += 1
        #     elif r == len(arr)-1 or (x - arr[l-1]) <= (arr[r+1] - x):
        #         l -= 1
        #     else:
        #         r+=1
        # return arr[l:r+1]
                
        