


def dfs(node, col,        color, adj):
    color[node] = col
    for neighbor in adj[node]:
        if color[neighbor] == -1:
            if not dfs(neighbor, 1 - col, color, adj):
            # if not dfs(neighbor, not col, color, adj):  # also rep as

                return False
        elif color[neighbor] == col:
            return False
    return True

def is_bipartite(V, adj):
    color = [-1] * V             
    
    for start in range(V):  # Handle disconnected graphs
        if color[start] == -1:
            if not dfs(start, 0, color, adj):
                return False
    return True

# Example usage
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

V = 4
adj = [[] for _ in range(V)]
add_edge(adj, 0, 2)
add_edge(adj, 0, 3)
add_edge(adj, 2, 3)
add_edge(adj, 3, 1)

print(1 if is_bipartite(V, adj) else 0)






