class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1idx = {n : i for i,n in enumerate(nums1)}
        result = [-1]* len(nums1)
        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val= stack.pop()
                idx = nums1idx[val]
                result[idx] = cur
            if cur in nums1idx:
                stack.append(cur)
                
        return result
            
        # result = [-1]*len(nums1)
        # for i in range(len(nums2)):
        #     if nums2[i] not in nums1idx:
        #         continue
        #     for j in range(i+1,len(nums2)):
        #         if nums2[j] >nums2[i]:
        #             index = nums1idx[nums2[i]]
        #             result[index] = nums2[j]
        #             break
        # return result
                    