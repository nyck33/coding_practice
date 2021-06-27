'''
Make as set of travel days
Then make cols for 0 to highest day of travel like knapsack
Then if day j is not in travel day, T(j) = T(j-1) ie. carry over
If day j is a travel day, try min{T(j-7) + costs[1], T(j-1) + costs[0],
T(j-30) + costs[2]}
'''
import sys


class Solution3:
    def mincostTickets(self, days: list, costs: list) -> int:
        daySet = set(days)
        size = max(days) + 1
        dp = [0] * size
        dp[0] = 0
        for i in range(1, size):
            if i in daySet:
                pass1 = dp[0] if i - 1 <= 0 else dp[i - 1]
                pass7 = dp[0] if i - 7 <= 0 else dp[i - 7]
                pass30 = dp[0] if i - 30 <= 0 else dp[i - 30]

                dp[i] = min(pass1 + costs[0], pass7 + costs[1], pass30 + costs[2])
            else:
                dp[i] = dp[i - 1]
        return dp[size - 1]

class MySolution:
    def mincostTickets(self, days, costs):
        travel_days = set(days)
        num_cols = max(travel_days) + 1
        T = [0 for x in range(num_cols)]
        T[0] = 0 # base case
        prev_day, prev_week, prev_mo = 0,0,0
        for i in range(1, len(T)):
            if i in travel_days:
                if i - 1 <= 0:
                    prev_day = 0
                else:
                    prev_day = T[i-1]
                if i - 7 <= 0:
                    prev_week = 0
                else:
                    prev_week = T[i-7]
                if i - 30 <= 0:
                    prev_mo = 0
                else:
                    prev_mo = T[i-30]

                T[i] = min(prev_day+costs[0], prev_week+costs[1],
                           prev_mo+costs[2])

            else:
                T[i] = T[i-1]

        return T[-1]


class Solution2:
    def mincostTickets(self, days: list, costs: list) -> int:
        # Dp array of cost per day from 0 to max value of days
        tot_cost = [0] * (days[-1] + 1)
        # Number of days per cost
        cost_d = [1, 7, 30]
        # If traveling 30 days is cheaper than 7 then, 7 days ticket is equal to 30 days ticket price
        if (costs[2] < costs[1]):
            costs[1] = costs[2]

        # If traveling 7 days is cheaper than 1 then, 1 day ticket is equal to 7 days ticket price
        if (costs[1] < costs[0]):
            costs[0] = costs[1]

        # Browse the array of days
        for r in range(1, len(days)):
            min_cost = sys.maxsize + 1
            # Take the minimum cost of days[r-1] checking all possible previous
            # cost from previous 2,7 or 30 days
            for k in range(len(costs)):
                min_cost = min(costs[k] + tot_cost[max(days[r - 1] - cost_d[k], 0)], min_cost)

            tot_cost[days[r - 1]] = min_cost
            # Keep unchanged the costs of the days not included in array days
            for d in range(days[r - 1] + 1, days[r]):
                tot_cost[d] = tot_cost[days[r - 1]]

        # Terminate with the last day of days
        min_cost = sys.maxsize + 1

        for k in range(len(costs)):
            min_cost = min(costs[k] + tot_cost[max(days[-1] - cost_d[k], 0)], min_cost)

        tot_cost[days[-1]] = min_cost

        return tot_cost[days[-1]]
class Solution:
    def mincostTickets(self, days: list, costs: list) -> int:
        '''
        T(i) = total cost for tickets to day i
        1, 7, 30 days
        '''
        T = [0 for x in range(len(days)+1)]
        days = [0] + days

        # on the 4th day better to buy one week pass
        # but iff all 4 days within 7
        day_pass, week_pass, month_pass = costs[0], costs[1], costs[2]
        # if week or month cheapest
        default_pass = min(costs)
        week_thresh = (week_pass // day_pass) + (week_pass % day_pass)
        month_thresh = (month_pass // day_pass) + (month_pass % day_pass)
        # but if day_pass more expensive
        if day_pass > week_pass:
            week_thresh = 1
        if day_pass > month_pass:
            month_thresh = 1

        for i in range(1, len(days)):
            # until threshold I can only buy separate day passes
            w_days, m_days = 0,0
            j = 1
            if i >= week_thresh:
                # k_days is num calendar days btwn thresholds for week
                # must be <=7
                # can go further back beyond threshold
                w_days = days[i] - days[i - week_thresh]
            # todo: while loop back as far as possible
            if i >= month_thresh:
                # m_days is num calendar days btwn the thresholds for month
                # must be <=30
                m_days = days[i] - days[i - month_thresh]
            # fill T(i)
            if i < week_thresh:
                T[i] = T[i-1] + costs[0]
            # from threshold and beyond
            #elif month_thresh > i >= week_thresh:
            #todo: speed up by using markers whenever week/mo pass bought
            elif i >= week_thresh:
                # check that first day is within 7 of day i
                if w_days <= 7:
                    # find an earlier day if possible
                    earliest = self.find_earliest(days, i, threshold=7)
                    if earliest is not None:
                        T[i] = min(T[i - 1] + default_pass, T[earliest] + week_pass)
                    else:
                        T[i] = T[i-1] + default_pass
                else:
                    T[i] = T[i-1] + default_pass

            if i >= month_thresh:
                # check first day is within 30 of day 1
                if m_days <= 30:
                    # find an earlier day if possible
                    earliest = self.find_earliest(days, i, threshold=30)
                    if earliest is not None:
                        temp = min(T[i-1] + default_pass, T[earliest] + month_pass)
                        if temp < T[i]:
                            T[i] = temp
                    else:
                        T[i] = T[i-1] + default_pass
                else:
                    T[i] = T[i-1] + default_pass
        return T[-1]

    def find_earliest(self, days, idx, threshold=7):
        '''
        Find earliest date that is within 7
        or 30 days range of end_date from days[end_idx - km_days]
        :param days: array of travel days
        :param idx: i - weeks_thresh or i - months_thresh
        :param threshold:
        :return: idx of days with earliest date within threshold of days[idx]
        '''
        # todo: while loop back as far as possible
        j = 1
        prevs = []
        end_date = days[idx]
        while True:
            #get date
            prev_idx = idx - j
            if prev_idx < 0:
                break
            prev = days[idx - j]
            if end_date - prev < threshold:
                prevs.append(idx-j)
            else:
                break
            j += 1
        if len(prevs) == 0:
            return None

        return prevs[-1]


if __name__ == "__main__":
    sol = Solution()
    # case 1: 11
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    #print(sol.mincostTickets(days, costs))
    #case 2: 17
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs = [2, 7, 15]
    #print(sol.mincostTickets(days, costs))

    days = [1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28]
    costs = [3,13,45]
    #print(sol.mincostTickets(days, costs))


    days = [1, 4, 6, 7, 8, 20]
    costs = [7, 2, 15]
    #print(sol.mincostTickets(days, costs))

    days = [1, 5, 8, 9, 10, 12, 13, 16, 17, 18, 19, 20, 23, 24, 29]
    costs = [3, 12, 54]
    #print(sol.mincostTickets(days, costs))
    my_sol = MySolution()
    print(my_sol.mincostTickets(days,costs))


