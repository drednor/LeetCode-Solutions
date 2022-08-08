class Twitter:

    def __init__(self):
        self.tweet = defaultdict(list)
        self.fol = defaultdict(set)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.time,tweetId])
        self.time-=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.fol[userId].add(userId)
        for followeeId in self.fol[userId]:
            if followeeId in self.tweet:
                index = len(self.tweet[followeeId]) - 1
                time, tweetid = self.tweet[followeeId][index]
                minheap.append([time, tweetid, followeeId, index-1])
        heapq.heapify(minheap)
        while minheap and len(res) <10:
            time , tweetid , followeeId, index = heapq.heappop(minheap)
            res.append(tweetid)
            if index >= 0:
                time , tweetid = self.tweet[followeeId][index]
                heapq.heappush(minheap,[time ,tweetid, followeeId, index-1])
        return res
                
                
            
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.fol[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.fol[followerId]:
            self.fol[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)