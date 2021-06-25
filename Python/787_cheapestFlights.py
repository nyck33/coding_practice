class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        # run Bellman Ford for k+1 edges
        # each flight is an edge
        num_flights = K + 1

        # make matrix with a row for 0 no edges
        # src column stays 0
        dist_mat = [[0 for x in range(n)] for y in range(num_flights+1)]

        # make adjacency matrix or list for graph
        num_edges = len(flights)
        # n * n adj matrix
        fwd_graph = [[None for x in range(n)] for y in range(n)]
        # need reverse graph
        rev_graph = [[None for x in range(n)] for y in range(n)]

        # iterate flights and fill adjacency matrix
        for i in range(len(flights)):
            curr_flight = flights[i]
            start, end, wt = curr_flight[0], curr_flight[1], curr_flight[2]
            fwd_graph[start][end] = wt
            #reverse graph
            end, start, wt = curr_flight[0], curr_flight[1], curr_flight[2]
            rev_graph[start][end] = wt


        for j in range(len(dist_mat[0])):
            dist_mat[0][j] = None # for infinity

        dist_mat[0][src] = 0
        
        dist = 0
        for i in range(1, num_flights+1):
            for z in range(len(dist_mat[i])):
                if z == src: # dist to source is always 0
                    dist_mat[i][z] = 0
                    continue
                # carry over dist from src to z
                dist_mat[i][z] = dist_mat[i-1][z]
                # all edges coming into vertex z, start at k
                kz_edges = rev_graph[z]
                for k in range(len(kz_edges)):
                    wt_kz = kz_edges[k] #wt from z to k fwd
                    if wt_kz is not None:
                        # not inf get dist from s to y
                        if dist_mat[i-1][k] is not None:
                            new_dist = dist_mat[i-1][k] + wt_kz
                        else: #dist to y is inf so inf + anything is inf
                            new_dist = None
                        if new_dist is not None and dist_mat[i][z] is None:
                            dist_mat[i][z] = new_dist

                        elif new_dist is None:
                            continue
                        # new_dist and prev dist are both not inf
                        elif new_dist < dist_mat[i][z]:
                            dist_mat[i][z] = new_dist


                        # else don't update the carry over
        # get the value for dist_mat[num_flights][dst]
        cost = dist_mat[num_flights][dst]
        if cost is None:
            return -1

        return cost

if __name__ == "__main__":
    sol = Solution()

    '''
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    
    cost = sol.findCheapestPrice(n, edges, src, dst, k)
    print(cost)
    '''
    n = 5
    edges = [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]]
    src = 2
    dst = 1
    k = 1

    cost = sol.findCheapestPrice(n, edges, src, dst, k)
    print(cost) # expects -1