    # indegree = [0] * V  # Initialize in-degree array
    # for i in range(V):
    #     for neighbor in adj[i]:
    #         indegree[neighbor] += 1

# ---------------------------------

# Find Eventual Safe States 
# - BFS - Topological Sort: G-25

  
from collections import deque

def eventual_safe_nodes(V, adj):
    adj_rev = [[] for _ in range(V)]
    indegree = [0] * V


# ----I M P O ----------------------------- 
               # Reverse the graph
    for i in range(V):
        for it in adj[i]:
            adj_rev[it].append(i)
            indegree[i] += 1
# --------------------------------- 
    q = deque()
    safe_nodes = []
    
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        safe_nodes.append(node)
        for it in adj_rev[node]:
            indegree[it] -= 1
            if indegree[it] == 0:
                q.append(it)
    
    return sorted(safe_nodes)

# Example usage
adj = [[1], [2], [3, 4], [4, 5], [6], [6], [7], [], [1, 9], [10], [8], [9]]
V = 12
safe_nodes = eventual_safe_nodes(V, adj)
print(safe_nodes)

