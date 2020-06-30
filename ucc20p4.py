import sys
input = sys.stdin.readline
N = int(input())
DP = [0] * (N+1)
prices = [0]
for i in range(N):
    prices.append(int(input()))

for i in range(1,N+1,1):
    if i == 1:
        DP[i] = prices[i]
    elif i == 2:
        DP[i] = prices[i - 1] + prices[i] - (min(prices[i - 1], prices[i])/4)
    elif i >= 3:
        DP[i] = min(DP[i - 1] + prices[i], min(DP[i-2]+prices[i-1]+prices[i]-min(prices[i-1],prices[i])/4 ,DP[i-3]+prices[i-2]+prices[i-1]+prices[i]-min(prices[i], min(prices[i-1], prices[i-2]))/2))
print(int(DP[N]))
