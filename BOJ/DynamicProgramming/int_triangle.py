# BOJ 1932, 정수 삼각형
import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp = []
arr = []
for i in range(1, n+1):
    # arr 값 입력 받기
    data = list(map(int, input().rstrip().split()))
    arr.append(data)
    # dp 0으로 초기화
    dp_row = [0] * i
    dp.append(dp_row)

# 초기값 설정
dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

print(max(dp[n-1]))