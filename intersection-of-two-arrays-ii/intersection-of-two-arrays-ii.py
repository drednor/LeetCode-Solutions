class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        c = Counter(nums1)
        for j in nums2:
            if c[j]>0:
                result.append(j)
                c[j] -= 1
        return result