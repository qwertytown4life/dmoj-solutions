import math
haystacks = int(input())
useless = int(input())
sizes = list(map(int, input().split()))
useless2 = int(input())
line = input()
max_imumLen = 0
temp = 0

line = line.replace('X','0')
derp = line.split('1')

listOfdist = []
for i in derp:
    if len(i) > 0:
        listOfdist.append(len(i))

notFound = False
listOfdist.sort()
theOne = 0

while not notFound:
    if sizes[-1] > listOfdist[-1]:
        sizes.pop(-1)
    else:
        theOne = sizes[-1]
        notFound = True

score = 0


print(math.ceil(haystacks/theOne))
