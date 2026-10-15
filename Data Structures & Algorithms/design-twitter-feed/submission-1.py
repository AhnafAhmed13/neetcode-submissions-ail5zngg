class Twitter:

    def __init__(self):
        self.tweets = []
        self.follower_dict = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        i = len(self.tweets) - 1
        while i >= 0 and len(res) < 10:
            tweetId, tweet_userId = self.tweets[i]
            if tweet_userId == userId or (userId in self.follower_dict and tweet_userId in self.follower_dict[userId]):
                res.append(tweetId)
            i -= 1
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower_dict:
            self.follower_dict[followerId] = set()
        self.follower_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower_dict:
            self.follower_dict[followerId].discard(followeeId)
