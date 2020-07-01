N = int(input())
size = N * 2
seen = []
l = 1; r = size - 1

while l <= r:
    row = ['*'] * size
    for i in range(l,r,1):
        row[i] = " "
    seen.append(''.join(row))
    l += 2
    r -= 2

for i in range(int(N/2) + 1):
    print(seen[i])

for i in range(int(N/2) - 1, - 1, -1):
    print(seen[i])
