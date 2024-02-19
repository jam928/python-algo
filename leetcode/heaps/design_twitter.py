# https://leetcode.com/problems/design-twitter/
import copy
from typing import List


class Twitter:

    def __init__(self):
        # store users and tweets in seperate map
        self.users_map = {}
        self.tweets_map = {}
        self.tweet_index = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # add tweets to tweets map
        tweets_list = self.tweets_map.get(userId, [])
        tweets_list.append((self.tweet_index, tweetId))
        self.tweets_map[userId] = tweets_list

        # update tweet_index
        self.tweet_index += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # merge all tweets from userid and its followers
        tweets = copy.deepcopy(self.tweets_map.get(userId, []))

        for user in self.users_map.get(userId, []):
            tweets.extend(self.tweets_map.get(user, []))

        # sort the tweets from most recent to least recent
        sorted_tweets = sorted(tweets, key=lambda x: x[0], reverse=True)

        # get the first 10 elements in the tweets list
        return [tweet[1] for tweet in sorted_tweets[0:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        # update the follower list of follower id in user map
        following_list = self.users_map.get(followerId, [])
        if followeeId not in following_list:
            following_list.append(followeeId)
            self.users_map[followerId] = following_list

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove the follower list of follower id in the user map
        following_list = self.users_map.get(followerId, [])
        if followeeId in following_list:
            following_list.remove(followeeId)
            self.users_map[followerId] = following_list

twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))  # Output: [5]
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))  # Output: [6, 5]
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))  # Output: [5]