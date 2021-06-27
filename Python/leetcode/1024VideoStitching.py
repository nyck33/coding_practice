'''
sort array by (start, end), put in dict {start: [clips]}
iterate and keep longest
Then for range (start + 1: end + 1), find next clip that gets me furthest
ie. the max
end + 1 is the latest start without a gap
then reset range to new_start + 1: end + 1
keep track of how many clips I use
'''
class Solution:
    def videoStitching(self, clips, T: int) -> int:
        '''
        clip could start and end on same [T, T]
        :param clips:
        :param T:
        :return:
        '''
        clips_d = {}
        for i in range(len(clips)):
            curr_clip = clips[i]
            start = curr_clip[0]
            end = curr_clip[1]
            if start not in clips_d:
                clips_d[start] = [end]
            else:
                clips_d[start].append(end)

        # keep the maxes
        for i in range(T+1):
            if i not in clips_d:
                continue
            curr_clips = clips_d[i]
            longest = max(curr_clips)
            clips_d[i] = longest

        # if zero not in clips_d, can't start at start
        if 0 not in clips_d:
            return -1
        # fill this in
        clips_used = []
        start_idx = 0
        end_idx = 0
        start = 0
        curr_end = 0
        next_end = 0
        num_clips = 0
        while True:
            if clips_d == {}:
                return -1
            if start_idx not in clips_d:
                start_idx += 1
                # there is a gap between end and next start
                if start_idx > curr_end:
                    return -1
            else:
                curr_end = clips_d[start_idx]
                # can delete key value pair from clips_d
                del clips_d[start_idx]
                # iterate back to start_idx + 1 to find the highest end
                high = float('-inf')
                for i in range(start_idx+1,curr_end+1):
                    # reached the end of event
                    if curr_end + 1 > T:
                        break
                    # no clip starts at i
                    if i not in clips_d:
                        continue

                    # check if next_end is max end
                    next_end = clips_d[i]
                    if next_end > high:
                        high = next_end
                        start = i

                num_clips += 1
                # for debugging
                clips_used.append([start_idx, curr_end])
                if curr_end >= T:
                    break

                start_idx = start

        return num_clips


if __name__=="__main__":
    sol = Solution()
    clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
    T = 10
    print(sol.videoStitching(clips, T))
    #3

    clips = [[0, 1], [1, 2]]
    T = 5
    print(sol.videoStitching(clips, T))
    # -1 clips don't reach T

    clips = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4],
             [4, 5], [5, 7], [6, 9]]
    T = 9
    print(sol.videoStitching(clips, T))
    #3

    clips = [[0, 4], [2, 8]]
    T = 5
    print(sol.videoStitching(clips, T))
    #2 clips end > T

    clips = [[0, 2], [4, 8]]
    T = 5
    print(sol.videoStitching(clips, T))
    #-1 gap

    clips = [[2, 4]]
    T = 0
    print(sol.videoStitching(clips, T))

    #-1

