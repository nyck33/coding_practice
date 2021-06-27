'''
min has to show how badly negative it gets during the trip
even if there is pos. after, it has to track the worst negative
min, ignore >=0, dictates moves for health
Then at end, I return abs(worst_min) + 1
'''
class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        '''
        start with 1*1, track min, ie. how low does it get in a path,
        take the path up to a square with lower min, make move, if new_health < min, update min
        Update T
        T(i,j) is the a tuple: (net health to get to (i,j) from (1,1), worst_min)
        Recurrence:
        Base: T(1,1) = dungeon(1,1) base_min = T(1,1)
        T(i,j) = T
        '''
        d = dungeon
        T = [[(0,0) for x in d[0]] for y in d]
        # flag to indicate health dipped <=0 during trip
        prev_health, prev_min, new_health, new_min = 0,0,0,0
        for i in range(len(d)):
            for j in range(len(d[i])):
                curr = dungeon[i][j]
                # base case, first worst_min is just the square val
                if i==0 and j==0:
                    #dip_count = self.check_dip(dip_count, curr_dung)
                    if curr < 0:
                        T[i][j] = (curr, curr) #, dip_count)
                    else:
                        T[i][j] = (curr, 0)
                    continue
                # top row
                if (i-1) < 0:
                    prev_health, prev_min = T[i][j-1]
                    new_health = prev_health + curr
                    #dip_count = self.check_dip(dip_count, new_health)
                    # the lowest health gets during trip
                    new_min = self.check_min(new_health, prev_min)
                    T[i][j] = (new_health, new_min) #, dip_count)
                # left col
                elif (j-1) < 0:
                    prev_health, prev_min = T[i-1][j]
                    new_health = prev_health + curr
                    #dip_count = self.check_dip(dip_count, new_health)
                    new_min = self.check_min(new_health, prev_min)
                    T[i][j] = (new_health, new_min)
                # others look left and up take from path of smallest small
                else:
                    prev_health_up, prev_min_up = T[i-1][j]
                    prev_health_left, prev_min_left = T[i][j-1]

                    if prev_health_up > prev_health_left:
                        prev_health = prev_health_up
                        prev_min = prev_min_up
                    elif prev_health_up <= prev_health_left:
                        prev_health = prev_health_left
                        prev_min = prev_min_left

                    new_health = prev_health + curr
                    new_min = self.check_min(new_health, prev_min)
                    T[i][j] = (new_health, new_min)

        rows = len(dungeon)
        cols = len(dungeon[0])

        final_health, final_min = T[rows-1][cols-1]
        return abs(final_min) + 1

    def check_min(self, new_health, prev_min):
        if new_health < 0 and new_health < prev_min:
            new_min = new_health
        else:
            new_min = prev_min
        return new_min


    def check_dip(self, dip_count, health):
        '''
        helper to see if health <=0 during trip.
        If not can start with 1 health
        :param health:
        :return::
        '''
        if health < 0:
            dip_count += 1
        return dip_count


if __name__=="__main__":
    sol= Solution()
    dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(sol.calculateMinimumHP(dungeon))
    # 7
    dungeon = [[0]]
    #print(sol.calculateMinimumHP(dungeon))
    #1
    dungeon = [[100]]
    #print(sol.calculateMinimumHP(dungeon))
    #1
    dungeon = [[-3,5]]
    #print(sol.calculateMinimumHP(dungeon))
    #4
    dungeon = [[-1,1]]
    #print(sol.calculateMinimumHP(dungeon))
    #2
    dungeon = [[0,5],[-2,-3]]
    #print(sol.calculateMinimumHP(dungeon))
    #1
    dungeon = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
    print(sol.calculateMinimumHP(dungeon))
