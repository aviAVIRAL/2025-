

# Shortest Path in
#    Undirected Graph 
#  with unit distance: G-28
# -------------------------------------
# simple representation 
# -------------------------------------

from collections import deque

def shortest_path(edges, N, M, src):
# ................................
    # Create an adjacency list for the undirected graph
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u) # impo undirected gp
# .................................
    # Distance array initialized with a large number
    dist = [float('inf')] * N
    dist[src] = 0
# .................................    
    # BFS toto_ sort 
    queue = deque([src])
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if dist[node] + 1 < dist[neighbor]:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
# ---------------------------------------
    # Convert unreachable nodes to -1
    return [d if d != float('inf') else -1 for d in dist]
    
    result = []
    for d in dist:
        if d != float('inf'):
            result.append(d)
        else: # GFG
            result.append(-1)
    return result

# Driver Code
N = 9
M = 10
edges = [(0, 1), (0, 3), (3, 4), (4, 5), (5, 6), (1, 2), (2, 6), (6, 7), (7, 8), (6, 8)]
# ATQ 
# unditredt grpah with unit weight 
sources = 0 
result = shortest_path(edges,N,M,sources)
print(result)
