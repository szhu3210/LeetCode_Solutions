class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets=collections.defaultdict(list)
        self.following=collections.defaultdict(set)
        self.timestamp=0
        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.timestamp-=1
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        heap=[]
        for user in set([userId])|self.following[userId]:
            for item in self.tweets[user][-1:-11:-1]:
                heapq.heappush(heap, item)
        res=[]
        for _ in range(10):
            if heap:
                res.append(heapq.heappop(heap)[1])
            else:
                break
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)