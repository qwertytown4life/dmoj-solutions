import sys
from collections import deque
raw_input = sys.stdin.readline
N = int(raw_input())
M = int(raw_input())
MAX = 1000005
vis = [0] * MAX
graph = [[] for i in range(MAX)]

def bfs(cur):
    q = deque()
    q.append(cur)
    while q:
        where = q.popleft()
        if where == M * N:
            return 'yes'
        for i in graph[where]:
            if not vis[i]:
                q.append(i)
                vis[i] = 1
    return 'no'

for i in range(1, N + 1, 1):
    row = list(map(int, raw_input().split()))
    for j in range(1, M + 1, 1):
        graph[i * j].append(row[j - 1])


print bfs(1)
