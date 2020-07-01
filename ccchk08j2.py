def digitSum(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum

ans = []
N = int(input())
for i in range(N):
    num = int(input())
    while len(str(num)) != 1:
        num = digitSum(num)
    ans.append(num)

for i in ans:
    print(i)
