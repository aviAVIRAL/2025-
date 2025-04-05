

# Detect Cycle in an Undirected Graph (using DFS)

def dfs(node, parent, vis, adj):
    vis[node] = 1  
    for adjacent_node in adj[node]:
        if not vis[adjacent_node]:  
            if dfs(adjacent_node, node, vis, adj):
                return True  
        elif adjacent_node != parent:  
            return True  
    return False  

def isCycle(V, adj):
    vis = [0] * V  
    for i in range(V):  
        if not vis[i]:  
            if dfs(i, -1, vis, adj):
                return True  
    return False  

# Example usage
V = 4
adj = [[], [2], [1, 3], [2]]  # List of lists representation
ans = isCycle(V, adj)

print(1 if ans else 0)
