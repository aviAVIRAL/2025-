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

    def addEdge(adj, u, v):
        adj[u].append(v)
        adj[v].append(u)

    addEdge(adj, 0, 1)
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 0, 4)

  #  print(adj)  # [ [ 1, 4], [0, 2, 3], [1], [1], [0]]
    
    ans = bfsOfGraph(n, adj)
    print(*ans)




# # ...
# from collections import deque

# def bfsOfGraph(n, adj):
#     vis = [0] * n
#     vis[0] = 1
#     q = deque()
#     q.append(0)
#     bfs = []
    
#     while q:
#         node = q.popleft()
#         bfs.append(node)
#         for neighbor in adj[node]:
#             if not vis[neighbor]:
#                 vis[neighbor] = 1
#                 q.append(neighbor)
#     return bfs

# if __name__ == "__main__":
#     n = 5
#     adj_list = [[] for _ in range(n)]  

#     def addEdge(u, v):
#         adj_list[u].append(v)
#         adj_list[v].append(u)

#     addEdge(0, 1)
#     addEdge(1, 2)
#     addEdge(1, 3)
#     addEdge(0, 4)

#     print(adj_list)  # Adjacency list representation
    
#     ans = bfsOfGraph(n, adj_list)
#     print(*ans)





