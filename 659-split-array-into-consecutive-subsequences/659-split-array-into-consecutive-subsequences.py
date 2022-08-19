class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        c = Counter(nums)
        end = defaultdict(int)
        for num in nums:
            if c[num]:
                c[num] -= 1
                if end[num-1]:
                    end[num-1] -= 1
                    end[num] += 1
                elif c[num+1] and c[num+2]:
                    c[num+1] -= 1
                    c[num+2] -= 1
                    end[num+2] += 1
                else:
                    return False
        return True