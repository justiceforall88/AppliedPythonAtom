#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.read_post = {}
        self.publish_post = {}
        self.follow_user = {}

    def user_posted_post(self, user_id: int, post_id: int):
        if user_id not in self.publish_post.keys():
            self.publish_post[user_id] = {post_id}
        else:
            self.publish_post[user_id].add(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        if user_id not in self.read_post.keys():
            self.read_post[user_id] = {post_id}
        else:
            self.read_post[user_id].add(post_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        if follower_user_id not in self.follow_user.keys():
            self.follow_user[follower_user_id] = {followee_user_id}
        else:
            self.follow_user[follower_user_id].add(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int)-> list:
        all_posts = set()
        for key, value in self.publish_post.items():
            if user_id in self.follow_user.keys():
                if key in self.follow_user[user_id]:
                    all_posts = all_posts.union(value)
        all_posts = sorted(list(all_posts), reverse=True)
        return all_posts[:k]

    def get_most_popular_posts(self, k: int) -> list:
        all_posts_count = {}
        for key, value in self. read_post.items():
            for a in value:
                if a not in all_posts_count.keys():
                    all_posts_count[a] = 1
                else:
                    all_posts_count[a] += 1
        all_posts_count = sorted(all_posts_count.items(), key=lambda kv: kv[1], reverse=True)
        answer = []
        cnt = 0
        for a in all_posts_count:
            answer.append(a[0])
            cnt += 1
            if cnt == k:
                return answer
