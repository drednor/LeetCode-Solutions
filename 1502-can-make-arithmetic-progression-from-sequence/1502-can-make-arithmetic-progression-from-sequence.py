class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort(reverse=True)
        check = arr[0] - arr[1]
        for i in range(1,len(arr)):
            if (arr[i-1] - arr[i]) == check:
                continue
            else:
                return False
        return True