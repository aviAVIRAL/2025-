

# Alien Dictionary - Topological Sort: G-26  



from collections import deque

def topo_sort(V, adj):
    indegree = [0] * V
    for i in range(V):
        for neighbor in adj[i]:
            indegree[neighbor] += 1
    
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    
    topo = []
    while q:
        node = q.popleft()
        topo.append(node)
        
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    
    return topo

def find_order(dict, N, K):
    adj = [[] for _ in range(K)]
    
    for i in range(N - 1):
        s1, s2 = dict[i], dict[i + 1]
        length = min(len(s1), len(s2))
        for ptr in range(length):
            if s1[ptr] != s2[ptr]:
                adj[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a'))
                break
    
    topo = topo_sort(K, adj)
    
    ans = "".join(chr(it + ord('a')) for it in topo)
    return ans

if __name__ == "__main__":
    N = 5
    K = 4
    dictionary = ["baa", "abcd", "abca", "cab", "cad"]
    
    result = find_order(dictionary, N, K)
    print(" ".join(result))

