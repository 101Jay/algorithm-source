# BOJ 2156, 포도주 시식
# dp[n] = max(dp[n-1], dp[n-2] + An, dp[n-3] + An-1 + An)
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]

dp = [0] * 10001
for i in range(1, n+1):
    if i <= 2:
        dp[i] = dp[i-1] + arr[i-1]
    else:
        dp[i] = max(dp[i-1], dp[i-2] + arr[i-1], dp[i-3] + arr[i-2] + arr[i-1]) # arr는 0번째 인덱스부터 시작함을 감안

print(dp[n])