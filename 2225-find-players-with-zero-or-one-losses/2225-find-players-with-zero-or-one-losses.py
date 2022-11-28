class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}
        ans = []
        for w, l in matches:
            if w not in winners:
                winners[w] = 0
            if l not in losers:
                losers[l] = 0
            winners[w] += 1
            losers[l] += 1
        wins = []
        oneloss = []
        for k, v in winners.items():
            if k not in losers:
                wins.append(k)
        
        for k, v in losers.items():
            if losers[k] == 1:
                oneloss.append(k)
        
        wins.sort()
        oneloss.sort()
        ans.append(wins)
        ans.append(oneloss)
        
        return ans