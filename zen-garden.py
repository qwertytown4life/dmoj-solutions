import sys
input = sys.stdin.readline

N = int(input())
flowers = list(map(int, input().split()))
total = sum(flowers)
for i in range(int(input())):
    flo, ded = map(int, input().split())
    total -= min(flowers[flo],flowers[flo-1],ded)
print(total)
