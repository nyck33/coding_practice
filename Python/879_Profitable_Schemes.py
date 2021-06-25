class Solution:
    def profitableSchemes(self, n, minProfit, group, profit) -> int:
        '''
        make graph and count how many paths there are under n,
        then for each path, make sets of the vertices,
        keep unique sets as there will be doubles of each path
        if vertices total > min_profit: num_schemes +=1
        '''
        graph = {}
        for i in range(len(profit)):
            u = profit[i]
            # each edge is weight, v
            graph[u] = [()]



if __name__=="__main__":
    sol = Solution()

    '''
    Output: 2
    Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
    In total, there are 2 schemes.
    '''
    n = 5
    minProfit = 3
    group = [2, 2]
    profit = [2, 3]
    print(sol.profitableSchemes(n,minProfit,group,profit))
    '''
    Output: 7
    Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
    There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
    '''
    n = 10
    minProfit = 5
    group = [2, 3, 5]
    profit = [6, 7, 8]
    print(sol.profitableSchemes(n,minProfit,group,profit))

