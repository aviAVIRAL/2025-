def dfs(node, adj, vis, ls):
    vis[node] = 1
    ls.append(node)
    # Traverse all its neighbors
    for neighbor in adj[node]:
        if not vis[neighbor]:
            dfs(neighbor, adj, vis, ls)

def dfsOfGraph(V, adj):
    vis = [0] * V  # Visited array
    ls = []  # List to store DFS traversal
    start = 0
    dfs(start, adj, vis, ls)
    return ls

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def printAns(ans):
    print(" ".join(map(str, ans)))  # Print DFS traversal

if __name__ == "__main__":
    adj = [[] for _ in range(5)]
    
    addEdge(adj, 0, 2)
    addEdge(adj, 2, 4)
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 3)

    # startNode = 0  # You can change this to any node you want
    ans = dfsOfGraph(5, adj)
    printAns(ans)
