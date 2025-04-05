




#  striver video repre 


from collections import deque

def shortest_path(edges, N, M, src):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    dist = [float('inf')] * N
    dist[src] = 0

    # Now storing (node, distance) in queue
    queue = deque( [ (src, 0) ] )
    # queue.append((src, 0))

    while queue:
        node, curr_dist = queue.popleft()
        for ngbr in adj[node]:
            if curr_dist + 1 < dist[ngbr]:
                dist[ngbr] = curr_dist + 1
                queue.append((ngbr, dist[ngbr]))  # pushing (node, updated distance)

    return [d if d != float('inf') else -1 for d in dist]

# Driver Code
N = 9
M = 10
edges = [(0, 1), (0, 3), (3, 4), (4, 5), (5, 6), (1, 2), (2, 6), (6, 7), (7, 8), (6, 8)]
source = 0

result = shortest_path(edges, N, M, source)
print(result)
