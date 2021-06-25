class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        '''
        T(i,w) = max{T(i, w-wi) + vi, T(i-1, w)} if w >= wi
        else: T(i,w) = T(i-1, w)
        '''
        coins = sorted(coins)
        T = [[0 for x in range(amount+1)] for y in range(len(coins)+1)]

        for i in range(1, len(coins)+1):
            for j in range(1,amount)