# Minimum steps to reach end from start by performing multiplication and mod operations with array elements

# Minimum Multiplications to Reach End


from collections import deque

class Solution:
    def minimumMultiplications(self, arr, start, end):
        q = deque()
        q.append((start, 0))

        dist = [float('inf')] * 100000
        dist[start] = 0
        mod = 100000

        while q:
            node, steps = q.popleft()

            for num in arr:
                new_num = (num * node) % mod

                if steps + 1 < dist[new_num]:
                    dist[new_num] = steps + 1

                    if new_num == end:
                        return steps + 1
                    q.append((new_num, steps + 1))

        return -1

# Driver code
if __name__ == "__main__":
    start = 3
    end = 30
    arr = [2, 5, 7]

    sol = Solution()
    ans = sol.minimumMultiplications(arr, start, end)
    print(ans)



