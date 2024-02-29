# BOJ 2839, 설탕 배달
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())
arr = [INF] * 5001

# 초기 데이터 입력
arr[3] = 1
arr[5] = 1

for i in range(6, n+1):
    #  점화식 : An = min(An-3, An-5) + 1
    arr[i] = min(arr[i-3], arr[i-5]) + 1

# 설탕 배달이 불가능한 경우 고려
if arr[n] >= INF:
    print(-1)
else:
    print(arr[n])