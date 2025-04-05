




def dijkstra( V, adj, Sour):
    s = set()
    dist = [float('inf')] * V
    dist[Sour] = 0
    s.add((0, Sour))

    while s:
# Find element with the smallest distance
        dis, node = min(s)  # min bhai 
        s.remove((dis, node))

        for ngr, W in adj[node]:
            if dis + W < dist[ngr]:
                if dist[ngr] != float('inf'):
                    s.remove((dist[ngr], ngr))
                dist[ngr] = dis + W
                s.add((dist[ngr], ngr))
    
    return dist

# Driver code
V, E, S = 3, 3, 2

# aslo rep  
# adj = {0: [(1, 1), (2, 6)], 1: [(2, 3), (0, 1)], 2: [(1, 3), (0, 6)]}

adj = [ [(1, 1), (2, 6)],  [(2, 3), (0, 1)],  [(1, 3), (0, 6)] ]


res = dijkstra(V, adj, S)
print(*res)


