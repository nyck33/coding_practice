graph = {1:[2,4], 2:[1,3], 3:[3,4],4:[1,3]}


def dfs(g, s=1):
    g[0] = [0]
    stack = []
    visited = [0 for x in range(len(g))]
    stack.append(s)

    while stack:
        u = stack.pop(-1)
        visited[u] = 1
        edges = g[u]
        for v in edges:
            if not visited[v]:
                stack.append(v)
    return visited

def bfs(g, s=1):
    g[0] = 0
    visited = [0 for x in range(len(g))]
    q = []
    q.append(s)

    while q:
        u = q.pop(0)
        visited[u] = 1
        edges = g[u]
        for v in edges:
            if not visited[v]:
                q.append(v)

    return visited

if __name__=="__main__":
    g = graph
    print(dfs(g))
    print(bfs(g))
