length = int(input())
mod = int(input())
ARRAY1 = list(map(int, input().split()))
VECTOR = []
for i in range(length):
    VECTOR.append((ARRAY1[i] % mod, ARRAY1[i]))

VECTOR.sort()
for i in range(length):
    print(VECTOR[i][1],end=' ')
