from collections import deque

def bfsOfGraph(n, adj):
    vis = [0] * n
    vis[0] = 1
    q = deque()
    q.append(0)
    bfs = []
    
    while q:
        node = q.popleft()
        bfs.append(node)
        for neighbor in adj[node]:
            if not vis[neighbor]:
                vis[neighbor] = 1
                q.append(neighbor)
    return bfs

    
if __name__ == "__main__":
    n = 5
    adj = [[] for _ in range(n)]  

    def addEdge(adj, u, v): # aslo rep
        adj[u].append(v)
        adj[v].append(u)

    addEdge(adj, 0, 1)
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 0, 4)

  #  print(adj)  # [ [ 1, 4], [0, 2, 3], [1], [1], [0]]
#     0
#    / \
#   1   4
#  / \
# 2   3
    ans = bfsOfGraph(n, adj)
    print(*ans)

