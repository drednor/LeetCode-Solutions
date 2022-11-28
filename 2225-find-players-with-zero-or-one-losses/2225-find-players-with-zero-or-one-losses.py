from sortedcontainers import SortedDict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost = SortedDict()                                  # [1] keeping track of all players
        
        for w,l in matches: 
            if w not in lost : lost[w] = 0                   # [2] add player 
            lost[l] = lost[l] + 1 if l in lost else 1        # [3] increase loss count
        
        zero = [k for k,l in lost.items() if lost[k] == 0]   # [4] filter winners..
        ones = [k for k,l in lost.items() if lost[k] == 1]   # [5] ...and losers
        
        return [zero, ones]