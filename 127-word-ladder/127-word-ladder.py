class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
                for j in range(len(cur)):
                    pattern = cur[:j] + "*" + cur[j+1:]
                    for nxt in nei[pattern]:
                        if nxt not in visit:
                            visit.add(nxt)
                            q.append(nxt)
                            
            res+=1
        return 0
        
            