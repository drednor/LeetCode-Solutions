class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, j = 0,0
        nums1, nums2 = sorted(nums1), sorted(nums2)
        result = []
        while i < len(nums1) and j <len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                result.append(nums1[i])
                i+=1
                j+=1
        return result
        
        
        
        
        ## Hash Map Solution
        # result = []
        # c = Counter(nums1)
        # for j in nums2:
        #     if c[j]>0:
        #         result.append(j)
        #         c[j] -= 1
        # return result