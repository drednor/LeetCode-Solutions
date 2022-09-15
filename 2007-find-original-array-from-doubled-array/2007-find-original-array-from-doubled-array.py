class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 == 1:
            return []
        changed.sort()
        c = Counter(changed)
        res = []
        for num in changed:
            if num == 0 and c[num]>=2:
                c[num]-=2
                res.append(num)
            elif num > 0 and c[num] and c[num*2]:
                c[num] -= 1
                c[num*2] -= 1
                res.append(num)
        return res if len(res) == len(changed)//2 else []
            
                
        