


# Topological Sort Algorithm | DFS: G-21

# dfs  


def dfs(node, vis, stack, adj):
    vis[node] = True
    for neighbor in adj[node]:
        if not vis[neighbor]:
            dfs(neighbor, vis, stack, adj)
    stack.append(node)  # Push to stack after visiting all neighbors

def topo_sort(V, adj):
    vis = [False] * V  # Visited array
    stack = []  # Stack to store topological order
    
    for i in range(V):
        if not vis[i]:
            dfs(i, vis, stack, adj)

    return stack[::-1]  # Reverse the stack to get correct order
# -------------------also rep--------
    ans = []
    while(stack):
        x = stack.pop()
        ans.append(x)
    return ans 
# ---------------------------
# Example usage
V = 6
adj = [[], [], [3], [1], [0, 1], [0, 2]]
ans = topo_sort(V, adj)
print(*ans)

