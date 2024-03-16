# BOJ 9461, 파도반 수열
import sys
input = sys.stdin.readline

tc = int(input().rstrip())

dp = [0] * 101
dp[1], dp[2], dp[3], dp[4], dp[5]  = 1, 1, 1, 2, 2

for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]

answer = []
for _ in range(tc):
    n = int(input().rstrip())
    answer.append(dp[n])

for ans in answer:
    print(ans)