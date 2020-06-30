import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
nodes = []
for i in range(N): nodes.append([])

for i in range(M):
    a, b, distance, speed = map(int, input().split())
    a -= 1
    b -= 1
    weight = round(distance / speed * 60)
    nodes[a].append((b, weight))
    nodes[b].append((a, weight))


def dij(graph, Num, srt, ending):
    dist = [float('inf')] * Num
    dist[srt] = 0
    q = [(srt, 0)]
    best = [float('inf')] * Num
    best[0] = 0

    while q:
        cur, time = q.pop(0)
        for i in graph[cur]:
            dis = dist[cur] + i[1]
            if dis <= dist[i[0]]:
                CurBest = time + 1
                best[i[0]] = CurBest
                dist[i[0]] = dis
                q.append((i[0],time + 1))
    return dist[ending], best[ending]


a, b = dij(nodes, N, 0, N - 1)

print(b)
print(round(a/0.75 - a))
