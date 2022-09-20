class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def check(nums1,nums2):
            n1 = len(nums1)
            n2 = len(nums2)
            res = 0
            for i in range(len(nums2)):
                counter = 0
                for j in range(len(nums1)):
                    if i + j >= n2:
                        break
                    if nums1[j] == nums2[i+j]:
                        counter+=1
                        res = max(counter,res)
                    else:
                        counter = 0
            return res
        return max(check(nums1,nums2),check(nums2,nums1))
                    
        
        
        
        
        # dp = [[0 for i in range(len(nums2)+1)] for j in range(len(nums1)+1)]
        # res = 0
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             dp[i+1][j+1] = dp[i][j] + 1
        #         res = max(dp[i+1][j+1],res)
        # return res
        
                
        