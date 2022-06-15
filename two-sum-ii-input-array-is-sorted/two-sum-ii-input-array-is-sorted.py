class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # TWO POINTER APPROACH
        i, j = 0, len(numbers)-1
        while i<j:
            if (numbers[i] + numbers[j]) > target:
                j-=1
            elif (numbers[i] + numbers[j]) < target:
                i+=1
            else:
                return [i+1,j+1]
        return []
        # SAME SOLUTION AS TWO SUM 1
        # somemap = {}
        # for i, n in enumerate(numbers):
        #     if (target-n) in somemap:
        #         return [somemap[target-n]+1,i+1]
        #     somemap[n] = i
        # return 