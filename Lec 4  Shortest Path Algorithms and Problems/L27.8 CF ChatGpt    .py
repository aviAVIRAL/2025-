


# Shortest Path in 
# Directed Acyclic Graph 
# Topological Sort: G-27




from collections import deque

def topo_sort(N, adj):
    vis = [0] * N
    stack = []
    
    def dfs(node):
        vis[node] = 1
        for v, _ in adj[node]:
            if not vis[v]:
                dfs(v)
        stack.append(node)
    
    for i in range(N):
        if not vis[i]:
            dfs(i)
    
    return stack[::-1]  # Reverse the stack to get topological order

def shortest_path(N, M, edges):
    # edge convert into adj list 
    adj = [[] for _ in range(N)]
    for u, v, wt in edges:
        adj[u].append((v, wt))
# --------------------------------
    top_order = topo_sort(N, adj)
    dist = [float('inf')] * N
    dist[0] = 0  # Assuming source is node 0
    
    for node in top_order:
        if dist[node] != float('inf'):
            for v, wt in adj[node]:
                if dist[node] + wt < dist[v]:
                    dist[v] = dist[node] + wt
    
    return [-1 if d == float('inf') else d for d in dist]

# Example usage
t = int(input())  # Number of test cases
for _ in range(t):
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    result = shortest_path(n, m, edges)
    print(*result)
