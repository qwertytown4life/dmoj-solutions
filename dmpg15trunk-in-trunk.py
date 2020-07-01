import sys
trunk = list(map(int, input().split()))
yourTrunk = list(map(int, input().split()))
trunk.sort()
yourTrunk.sort()
for i in range(3):
    if trunk[i] > yourTrunk[i]:
        print('N')
        sys.exit()
print('Y')
