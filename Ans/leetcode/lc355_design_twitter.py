class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = {}     # userId -> [(time, tweetId), ...] 投稿順
        self.following = {}  # userId -> {followeeId: True, ...}（dictをset代わりに使う）

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        if user_id not in self.tweets:
            self.tweets[user_id] = []
        self.tweets[user_id].append((self.time, tweet_id))
        self.time += 1

    def get_news_feed(self, user_id: int) -> list[int]:
        relevant_users = {user_id: True}
        if user_id in self.following:
            for followee in self.following[user_id]:
                relevant_users[followee] = True

        candidates = []
        for u in relevant_users:
            if u in self.tweets:
                for entry in self.tweets[u]:
                    candidates.append(entry)

        # 上位10件を選択ソートで取り出す（sorted()は使わない）
        result = []
        take = 10 if len(candidates) > 10 else len(candidates)
        for _ in range(take):
            best_idx = 0
            for i in range(1, len(candidates)):
                if candidates[i][0] > candidates[best_idx][0]:
                    best_idx = i
            result.append(candidates[best_idx][1])
            candidates.pop(best_idx)
        return result

    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id not in self.following:
            self.following[follower_id] = {}
        self.following[follower_id][followee_id] = True

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if follower_id in self.following and followee_id in self.following[follower_id]:
            del self.following[follower_id][followee_id]
