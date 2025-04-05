



# Kahn's Algorithm | Topological Sort Algorithm | BFS:
# BFS  
from collections import deque

def topo_sort(V, adj):
    # Compute in-degree for each node
    indegree = [0] * V  # Initialize in-degree array
    for i in range(V):
        for neighbor in adj[i]:
            indegree[neighbor] += 1

    # Push nodes with in-degree 0 into the q
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    topo = []  # Store topological order
    while q:
        node = q.popleft()
        topo.append(node)

        # Reduce in-degree of adjacent nodes
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
 
    return topo

# Example usage
V = 6
adj = [[], [], [3], [1], [0, 1], [0, 2]]

ans = topo_sort(V, adj)
print(*ans)




