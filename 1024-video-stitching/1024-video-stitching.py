class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        count = 0
        end = 0
        i = 0
        n = len(clips)

        while end < time:
            farthest = end

            while i < n and clips[i][0] <= end:
                if clips[i][1] > farthest:
                    farthest = clips[i][1]
                i += 1

            if farthest == end:
                return -1

            end = farthest
            count += 1

        return count