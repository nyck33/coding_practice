"""
use union find and return num of unique roots
which means I have to run find on every node since union does not update
parents to root until are_connected called next
just call find directly
"""
class Solution:
    def findCircleNum(self, isConnected) -> int:
        rank = [0 for i in range(len(isConnected))]
        pi = [i for i in range(len(isConnected))]

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]: # 1 is entry
                    if not self.are_connected(i,j, pi):
                        self.union(i,j,pi,rank)

        # iterate pi to update all parents
        for k in range(len(isConnected)):
            node = k
            dummy = self.find(node, pi)

        # find unique roots for num provinces
        roots_set = set(pi)

        return len(roots_set)

    # union self.find to check connectivity
    def are_connected(self, u, v, pi):
        root_u = self.find(u, pi)
        root_v = self.find(v, pi)
        if root_u == root_v:
            return True
        return False

    def find(self, vert, pi):
        if vert != pi[vert]:
            pi[vert] = self.find(pi[vert], pi)

        return pi[vert]

    def union(self, u, v, pi, rank):
        root_u = self.find(u, pi)
        root_v = self.find(v, pi)

        if root_u == root_v:
            return
        if rank[root_u] > rank[root_v]:
            pi[root_v] = root_u
        else:
            pi[root_u] = root_v
            if rank[root_u] == rank[root_v]:
                rank[root_v] += 1

if __name__=="__main__":
    sol = Solution()
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(sol.findCircleNum(isConnected))
    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(sol.findCircleNum(isConnected))
