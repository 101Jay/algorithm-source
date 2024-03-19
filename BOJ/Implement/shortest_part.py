# BOJ 11053, 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = list(map(int, input().rstrip().split()))

dp = [[] for _ in range(n+1)]
dp[1] = [1, data[0]]

for i in range(2, n+1):
    max_val = 0
    cur_size = data[i-1]
    # dp 값 갱신
    for j in range(1, i):
        if data[j-1] < cur_size and max_val < dp[j][0] + 1:
            max_val = dp[j][0] + 1

    # 해당 값보다 작은 것이 없었다면
    if max_val == 0:
        # 그 자체로 혼자 가장 긴 증가하는 부분 수열
        dp[i] = [1, data[i-1]]
    else:
        dp[i] = [max_val, data[i-1]]

# 최댓값 찾기
answer = 0
for i in range(1, n+1):
    if dp[i][0] > answer:
        answer = dp[i][0]

print(answer)