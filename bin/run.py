import argparse

import tweepy

from randombird import TweetListener


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="consumer_key")
    parser.add_argument("--secret", help="consumer_secret")
    parser.add_argument("--token", help="access_token")
    parser.add_argument("--token_secret", help="access_token_secret")
    args = parser.parse_args()

    auth = tweepy.OAuthHandler(args.key, args.secret)
    auth.set_access_token(args.token, args.token_secret)

    stream = tweepy.Stream(auth, TweetListener(tweepy.API(auth)))

    stream.filter(locations=[-78.1, 38.0, -74.0, 40.7, ])
#     lrange random 0 -1


if __name__ == '__main__':
    main()
