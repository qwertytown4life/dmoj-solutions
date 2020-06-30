number_of_lifts = int(input())
min_sum = float('inf')

for i in range(number_of_lifts):
    montain = list(map(int, input().split()))
    temp = sum(montain) - montain[0]
    min_sum = min(min_sum, temp)

print(min_sum)
