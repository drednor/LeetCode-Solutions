class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A , B = nums1 , nums2
        total = len(A)+len(B)
        half = total//2
        if len(A)>len(B):
            A,B = B,A
        l, r = 0, len(A)-1
        while True:
            i = (l+r)//2
            j = half - i -2

            aleft = A[i] if i >= 0 else float("-infinity")
            aright = A[i+1] if i+1 <len(A) else float("infinity")
            bleft = B[j] if j >= 0 else float("-infinity")
            bright = B[j+1] if j+1 <len(B) else float("infinity")

            if aleft <= bright and bleft<=aright:
                if total%2:
                    return min(aright, bright)
                else:
                    return (max(aleft,bleft) + min(aright,bright))/2
            elif aleft>bright:
                r = i -1
            else:
                l = i +1
#         A , B = nums1 , nums2
#         total = len(A) + len(B)
#         half = total//2
        
#         if len(B)< len(A):
#             A,B = B,A
            
#         l , r = 0 , len(A)-1
#         while True:
#             i = (l+r)//2
#             j = half -i -2
            
#             aleft = A[i] if i>=0 else float("-infinity")
#             aright = A[i+1] if (i+1) < len(A) else float("infinity")
#             bleft = B[j] if j>=0 else float("-infinity")
#             bright = B[j+1] if (j+1) < len(B) else float("infinity")
            
#             #partition is correct
#             if aleft <= bright and bleft<= aright:
#                 #odd
#                 if total%2:
#                     return min(aright, bright)
#                 else:
#                 #even
#                     return (max(aleft,bleft)+min(aright,bright))/2
#             elif aleft>bright:
#                 r = i-1
#             else:
#                 l = i+1
        
        
        
        
#         nums = sorted(nums1 + nums2)
#         l , r = 0 , len(nums)-1
#         mid = l+r
#         if mid % 2 == 1:
#             mid = mid//2
#             return (nums[mid]+nums[mid+1])/2
#         else:
#             mid = mid//2
#             return nums[mid]
        
        