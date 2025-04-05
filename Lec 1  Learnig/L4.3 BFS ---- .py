

from collections import deque

def bfsOfGraph(n, adj, start):
    vis = [0] * n
    vis[start] = 1
    q = deque() # q = deque([start])
    q.append(start) # 
    bfs = []
       
    while q:
        node = q.popleft()
        bfs.append(node)
        for neighbor in adj[node]:
            if not vis[neighbor]:
                vis[neighbor] = 1
                q.append(neighbor)
    return bfs

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    n = 5
    adj = [[] for _ in range(n)]
    
    addEdge(adj, 0, 1)
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 0, 4)

    start_node = 0 # Changed the starting node to 4 : therfrore op is [4,0,1,2,3]
    ans = bfsOfGraph(n, adj, start_node)
    print(ans)  
     #  print(adj)  # [ [ 1, 4], [0, 2, 3], [1], [1], [0]]
#     0
#    / \
#   1   4
#  / \
# 2   3


# ...

    # also 
    
    # print(*ans)
    
    # for x in ans : 
    #     print(ans, end= " ")
    # print()

