import hashlib

import redis
import tweepy


def parse_tweet(t):
    print(t)
    h = hashlib.sha256()
    h.update(t.encode('utf-8'))
    print(len(h.digest()), h.digest())
    return h.digest()


class TweetListener(tweepy.StreamListener):

    def __init__(self, api=None):
        super().__init__(api)

        self.r = redis.Redis(
            # host='hostname',
            # port=port,
            # password='password'
        )

    def on_data(self, raw_data):
        self.r.rpush("random", parse_tweet(raw_data))

    # def on_status(self, status):
    #     print(status.text)

