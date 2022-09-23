class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets)==1:
            if triplets[0] == target:
                return True
            else:
                return False
        one = False
        two = False
        three = False
        check = []
        for x in triplets:
            if x[0] <= target[0]:
                if x[1] <= target[1]:
                    if x[2] <= target[2]:
                        if x[0] == target[0]:
                            one = True
                        if x[1] == target[1]:
                            two = True
                        if x[2] == target[2]:
                            three = True
                        if one and two and three:
                            return True
        return False
        
        
            