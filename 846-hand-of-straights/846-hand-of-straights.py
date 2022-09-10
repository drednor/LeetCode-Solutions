class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        c = Counter(hand)
        hand.sort()
        for i in range(len(hand)):
            temp = hand[i]
            if temp not in c:
                continue
            j = 0
            while j < groupSize:
                if temp+j not in c:
                    return False
                c[temp+j] -= 1
                if c[temp+j] == 0:
                    del c[temp+j]
                j+=1
        return True
                