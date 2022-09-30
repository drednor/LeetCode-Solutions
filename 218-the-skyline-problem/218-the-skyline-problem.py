from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = collections.defaultdict(list)
        for left, right, height in buildings:
            events[left].append((-1,height))
            events[right].append((1,height))
        
        sl = SortedList()
        sl.add(0)
        
        res = []
        last_height = 0
        for x in sorted(events.keys()):
            for t, h in events[x]:
                if t == -1:
                    sl.add(h)
                else:
                    sl.remove(h)
            current_height = sl[-1]
            if current_height != last_height:
                res.append([x,current_height])
            last_height = current_height
        return res
            