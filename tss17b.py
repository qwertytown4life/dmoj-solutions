import bisect
import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
dist = []
for i in range(N):
    x, y = map(int, input().split())
    dist.append((x**2 + y**2)**0.5)

dist.sort()

for i in range(Q):
    a = int(input())
    print(bisect.bisect_right(dist, a))
