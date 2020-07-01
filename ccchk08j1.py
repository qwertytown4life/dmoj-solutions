cas = 0
nat = 0
C = int(input())
for i in range(C):
    a, b = map(int, input().split())
    cas = max(cas, a * b)

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    nat = max(nat, a * b)

if nat > cas:
    print('Natalie')
elif cas > nat:
    print('Casper')
else:
    print('Tie')
