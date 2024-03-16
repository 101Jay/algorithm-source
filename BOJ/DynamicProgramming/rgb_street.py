# BOJ 1149, RGB거리
import sys, copy
input = sys.stdin.readline
n = int(input().rstrip())

data = []
for _ in range(n):
    row = list(map(int, input().rstrip().split()))
    data.append(row)

dp = [[0, 0, 0] for _ in range(n)]
dp[0] = copy.deepcopy(data[0])

for i in range(1, n):
    dp[i][0] = data[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = data[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = data[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))