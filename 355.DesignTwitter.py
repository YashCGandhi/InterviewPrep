class Twitter:

    def __init__(self):
        self.tweets = []
        self.connections = defaultdict(list)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for i in range(len(self.tweets)-1,-1,-1):
            if len(feed) == 10:
                return feed
            elif self.tweets[i][0] == userId or self.tweets[i][0] in self.connections[userId]: 
                feed.append(self.tweets[i][1])
        return feed
    def follow(self, followerId: int, followeeId: int) -> None:
        self.connections[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followees = self.connections[followerId]
        if followeeId in followees:
            followees.remove(followeeId)
        for f in followees:
            self.connections[followerId].append(f)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
