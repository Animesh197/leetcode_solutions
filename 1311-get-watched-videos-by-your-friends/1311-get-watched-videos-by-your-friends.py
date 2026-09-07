class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        n = len(friends)

        queue = [id]
        visited = [False] * n
        distance = [0] * n

        visited[id] = True
        index = 0

        while index < len(queue):
            person = queue[index]
            index += 1

            for friend in friends[person]:
                if not visited[friend]:
                    visited[friend] = True
                    distance[friend] = distance[person] + 1
                    queue.append(friend)

        count = {}

        for person in range(n):
            if distance[person] == level:
                for video in watchedVideos[person]:
                    if video in count:
                        count[video] += 1
                    else:
                        count[video] = 1

        videos = list(count.keys())

        videos.sort(key=lambda x: (count[x], x))

        return videos