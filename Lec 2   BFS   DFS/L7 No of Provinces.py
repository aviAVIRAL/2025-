

def dfs(node, adjLs, vis):
    # Mark the node as visited
    vis[node] = True
    for neighbor in adjLs[node]:
        if not vis[neighbor]:
            dfs(neighbor, adjLs, vis)

def num_provinces(adj, V):
    #a slo rep 
    # adjLs = {i: [] for i in range(V)} \\ aslo rep op {0: [], 1: [], 2: []}
    adjLs = [[] for _ in range(V)]   # op [[], [], []]
    
    # concopt
    # adjLs = [ ]*V  # no non  not represent like thsi baby 
    # adjLs = [[]*2] not eork 
    
    # Convert adjacency matrix to adjacency list
    for i in range(V):
        for j in range(V):
            if adj[i][j] == 1 and i != j: #  impo  adj[i][j]   adjLS nhi hai ye 
                adjLs[i].append(j)
                adjLs[j].append(i)

    print(adjLs)
    # vis = [False] * V  als0 rep 
    vis = [0] * V
    count = 0

    for i in range(V):
        if not vis[i]:
            count += 1
            dfs(i, adjLs, vis)
    return count

if __name__=="__main__":
    # Example usage      adja matrix ki form mein given hai bhai adjecency            
    adj = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    print(num_provinces(adj, 3))


