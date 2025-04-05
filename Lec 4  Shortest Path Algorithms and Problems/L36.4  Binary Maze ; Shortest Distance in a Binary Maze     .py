
# G-36: Shortest Distance in a 
# Binary Maze 


from collections import deque

def shortest_path(grid, source, destination):
    # Edge Case: if the source is only the destination.
    if source == destination:
        return 0

    n, m = len(grid), len(grid[0])

    # Queue for BFS: (distance, (row, col))
    q = deque()
    q.append((0, source))

    # Distance matrix
    dist = [[float('inf')] * m for _ in range(n)]
    dist[source[0]][source[1]] = 0

    # Directions: up, right, down, left
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while q:
        dis, (r, c) = q.popleft()

        for i in range(4):
            newr, newc = r + dr[i], c + dc[i]

            if 0 <= newr < n and 0 <= newc < m and grid[newr][newc] == 1 and dis + 1 < dist[newr][newc]:
                dist[newr][newc] = dis + 1
                if (newr, newc) == destination:
                    return dis + 1
                q.append((dis + 1, (newr, newc)))

    return -1

# Driver Code
grid = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 0, 0, 1]
]

source = (0, 1)
destination = (2, 2)

res = shortest_path(grid, source, destination)
print(res)



