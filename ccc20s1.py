numberOfRuns = int(input())
vector = []
maxSpeed = 0
for i in range(numberOfRuns):
    time, distance = map(int, input().split())
    vector.append((time, distance))
vector.sort()
for i in range(numberOfRuns - 1):
    maxSpeed = max(maxSpeed,round(abs(vector[i][1] - vector[i + 1][1]) / abs(vector[i][0] - vector[i + 1][0]),100))
print(maxSpeed)
