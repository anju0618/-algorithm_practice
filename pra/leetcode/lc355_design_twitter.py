class Twitter:
    def __init__(self):
        # TODO: implement (per-user tweet log + follow graph via dict)
        pass

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        pass

    def get_news_feed(self, user_id: int) -> list[int]:
        pass

    def follow(self, follower_id: int, followee_id: int) -> None:
        pass

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    tw = Twitter()
    tw.post_tweet(1, 5)
    check("own tweet only", tw.get_news_feed(1), [5])
    tw.follow(1, 2)
    tw.post_tweet(2, 6)
    check("with followee tweet", tw.get_news_feed(1), [6, 5])
    tw.unfollow(1, 2)
    check("after unfollow", tw.get_news_feed(1), [5])
