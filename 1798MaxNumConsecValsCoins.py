'''
Get all unique combinations of the coins using DP
(1,1,1,4): (), (1)/ (1), (1), (1,1)/ (1), (1,1), (1,1), (1,1,1)/
(4), (1,1,1,4), (1,1,4), (1,4)
SO
T(i) = the new sets I can make with the addition of
coin i
Recurrence:
T(i) = for set in sets in T(j): set + coins(i)
for 1 <= j <= i-1
To get rid of repeats, make a set of subsets,
then sum each subset, then sort and iterate res
'''

class Solution:
    def getMaximumConsecutive(self, coins: list) -> int:
        '''
        :param coins:
        :return: num_consecutive
        '''
        # list of lists of coin combos
        T = [[],[coins[0]]]
        for i in range(1, len(coins)):
            curr = coins[i]
            new_combos = []
            new_combos.append([curr])
            #exponential time here
            for j in range(len(T)-1, -1, -1):
                prev_combo = T[j]
                new_combo = prev_combo + [curr]
                new_combos.append(new_combo)
            T = T + new_combos

        #get sums and sort
        totals = [0 for x in T]
        for m in range(len(T)):
            curr_total = sum(T[m])
            totals[m] = curr_total

        #eliminate duplicates
        totals = set(totals)
        totals = sorted(list(totals))

        #iterate to count consecutives
        long = len(totals)
        #new table, base case is T(1) = 1
        num_consec = [0 for x in totals]
        num_consec[0] = 1

        for i in range(1, len(totals)):
            if (totals[i] - 1) == totals[i-1]:
                num_consec[i] = num_consec[i-1] + 1
            else:
                num_consec[i] = 0

        return max(num_consec)

if __name__=="__main__":
    sol = Solution()
    coins = [1,1,1,4]
    print(sol.getMaximumConsecutive(coins))

    coins = [1,89,8,1,47,34,99,1,1,1,55,89,1,52,36,1,62,1,1,1,4,27,1,45,1,1,48,1,94,1,63]
    print(sol.getMaximumConsecutive(coins))




