class Solution:
    def averageWaitingTime(self, customers) -> float:
        '''
        arrival = [x for [x,_] in customers]
        cook_time = [x for [_,x] in customers]
        T = [3, 8, 11] arrival plus cooking time
        base case T(1) = arrival(1) + ctime(1)
        For 2 <= i <= n:
        T(i) = T(i-1) + ctime(i)
        arrivals = [1, 2, 4]

        Wait = [2, 6, 7]
        For 1 <= i <= n:
        Wait(i) = T(i) - arrivals(i)
        '''
        arrivals = [x for [x, _] in customers]
        ctime = [x for [_, x] in customers]

        Waits = [0 for x in ctime]
        food_done = [0 for x in ctime]
        # base case
        food_done[0] = arrivals[0] + ctime[0]
        for i in range(1, len(arrivals)):
            # arrives before or when previous meal done
            if arrivals[i] - food_done[i-1] <=0:
                food_done[i] = food_done[i - 1] + ctime[i]
            else:
                food_done[i] = arrivals[i] + ctime[i]

        for j in range(len(food_done)):
            Waits[j] = food_done[j] - arrivals[j]

        avg = round(sum(Waits) / len(food_done), 5)

        return avg

if __name__=="__main__":
    sol = Solution()
    customers = [[1, 2], [2, 5], [4, 3]]
    print(sol.averageWaitingTime(customers))

    customers = [[5,2],[5,4],[10,3],[20,1]]
    print(sol.averageWaitingTime(customers))