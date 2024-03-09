# BOJ 12865, 평범한 배낭
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = []
for _ in range(n):
    weight, value = map(int, input().rstrip().split())
    arr.append((weight, value))

dp = [[0] * (k+1) for _ in range(n+1)]

for max_w in range(k+1):
    for h, tup in enumerate(arr):
        w, v = tup
        i = h+1

        if max_w - w >= 0:
            dp[i][max_w] = max(dp[i-1][max_w], dp[i-1][max_w - w] + v)
        else:
            dp[i][max_w] = dp[i-1][max_w]

print(dp[n][k])