'''
Define Table:
T(i) = num consecutive I can make with A(1...i)
Recurrence Relation:
Base Case:
T(0) = 1 #no coins makes 1 consecutive of zero
For i = 1 to n:
T(i) = T(i-1) + coins(i) if coins(i) <= T(i-1)
else: return T(i-1)

'''

class Solution:
    def getMaximumConsecutive(self, coins: list) -> int:
        T = [0 for x in range(len(coins)+1)]
        # no coins is 1 consecutive number of 0, base case
        T[0] = 1
        # ascending
        coins.sort()
        coins = [0] + coins
        for i in range(1, len(coins)):
            if coins[i] <= T[i-1]:
                T[i] = T[i-1] + coins[i]
            else:
                return T[i-1]
        #made it through entire list of coins so return last
        return T[len(coins)-1]
if __name__=="__main__":
    sol = Solution()
    coins = [1,3]
    print(sol.getMaximumConsecutive(coins))

    coins = [1,1,1,4]
    print(sol.getMaximumConsecutive(coins))

    coins = [1, 4, 10, 3, 1]
    print(sol.getMaximumConsecutive(coins))
    # 20


    coins = [1,89,8,1,47,34,99,1,1,1,55,89,1,52,36,1,62,1,1,1,4,27,1,45,1,1,48,1,94,1,63]
    print(sol.getMaximumConsecutive(coins))




