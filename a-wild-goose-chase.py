N, T = map(int, input().split())
table = []
for i in range(N):
    table.append(0)

plus_score = 0

for i in range(N):
    which_fox, accusing = map(int, input().split())
    if accusing == -1:
        table[which_fox - 1] -= 1
        plus_score += 1
    else:
        table[accusing - 1] += 1

for i in range(len(table)):
    table[i] += plus_score

GUILTY = []

for i in range(len(table)):
    if table[i] == T:
        GUILTY.append(i + 1)

if len(GUILTY) <= 0:
    print('-1')
else:
    print(' '.join(map(str, GUILTY)))
