class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        '''
        T(i) is the total num bricks to get to heights(1...i)
        If I'm short of bricks, replace the
        see how far you get with bricks, run out, go back and use ladder on tallest
        updated
        repeat
        '''
        # track how many bricks at j I need to get to j+1
        # last idx does not need any bricks
        #climbs[-1] is unused, no more to climb
        climbs = [0 for x in range(len(heights))]
        for i in range(0, len(heights)-1):
            climb = heights[i+1] - heights[i]
            if climb > 0:
                climbs[i] = climb
        
        rem_bricks = bricks
        rem_ladders = ladders
        #track total num bricks used
        T = [0 for x in heights]
        # base case is T[0] = 0
        # track heights covered by bricks
        # bricks = num_bricks, ladder = float('-inf')
        reached = -1
        keep_going = True
        for j in range(0, len(climbs)-1):
            if climbs[j] > 0:
                # enough bricks
                if rem_bricks - climbs[j] >= 0:
                    rem_bricks -= climbs[j]
                    T[j+1] = T[j] + climbs[j]
                    reached = j + 1
                else: # less bricks than current climb
                    while True:
                        #put up enough ladders to get enough bricks
                        if rem_ladders <= 0:
                            reached = j
                            keep_going = False
                            break
                        #j+1 so can use ladder current climb
                        highest = max(climbs[:j + 1])
                        high_idx = climbs.index(highest)
                        climbs[high_idx] = float('-inf')
                        rem_ladders -= 1
                        # can't add bricks if it's current climb
                        if high_idx < j:
                            rem_bricks += highest
                            T[j] -= highest
                            if rem_bricks >= climbs[j]:
                                rem_bricks -= climbs[j]
                                T[j + 1] = T[j] + climbs[j]
                                reached = j + 1
                                break
                        else: # high_idx == j
                            T[j+1] = T[j]
                            reached = j+1
                            break
            else:
                T[j+1] = T[j]
                if (j+1) >= len(climbs) -1:
                    reached = len(climbs)-1
                    keep_going = False


            if not keep_going:
                break
        return reached


if __name__=="__main__":
    sol = Solution()
    #heights
    h = [4, 2, 7, 6, 9, 14, 12]
    ##bricks
    b = 5
    #ladders
    l = 1
    print(sol.furthestBuilding(h, b, l))
    #4

    h = [4, 12, 2, 7, 3, 18, 20, 3, 19]
    b = 10
    l = 2
    print(sol.furthestBuilding(h, b, l))
    #7

    h = [14, 3, 19, 3]
    b = 17
    l = 0
    print(sol.furthestBuilding(h, b, l))
    #3

    h = [3, 19]
    b = 87
    l = 1
    print(sol.furthestBuilding(h, b, l))
    #1
