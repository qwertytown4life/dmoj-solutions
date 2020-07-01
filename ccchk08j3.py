suspects = []
peps = []
times = {}
people = int(input())
for i in range(people):
    name, number = input().split()
    peps.append((name,number))
    times[number] = 0

Q = int(input())
for i in range(Q):
    called = input()
    if called in times:
        times[called] += 1

a = float('-inf')

for key in times:
    a = max(a, times[key])

for key in times:
    if times[key] == a:
        suspects.append(key)

suspects.sort()
theAns = suspects[0]

for i in peps:
    if i[1] == theAns:
        print(i[0])
