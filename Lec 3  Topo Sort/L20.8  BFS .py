


# L 25   
# mein using toposort kiya hai 

# bfs 

from collections import deque

def eventual_safe_nodes(V, adj):
    adj_rev = [[] for _ in range(V)]  # Reverse adjacency list
    indegree = [0] * V  # Indegree array
    
    # Build reversed graph and compute indegrees
    for i in range(V):
        for neighbor in adj[i]:
            adj_rev[neighbor].append(i)
            indegree[i] += 1

    # Queue for processing nodes with 0 indegree
    queue = deque()
    safe_nodes = []
    
    for i in range(V):
        if indegree[i] == 0:
            queue.append(i)

    # Process nodes in topological order
    while queue:
        node = queue.popleft()
        safe_nodes.append(node)
        
        for neighbor in adj_rev[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return sorted(safe_nodes)  # Return sorted list of safe nodes

# Example usage
V = 12
adj = [[1], [2], [3, 4], [4, 5], [6], [6], [7], [], [1, 9], [10], [8], [9]]

safe_nodes = eventual_safe_nodes(V, adj)
print(*safe_nodes)
















