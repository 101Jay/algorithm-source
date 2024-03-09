# BOJ 9095, 1,2,3 더하기
import sys
input = sys.stdin.readline

tc = int(input().rstrip())
data = []
for _ in range(tc):
    n = int(input().rstrip())
    data.append(n)

max_n = max(data)

# 점화식에 사용할 배열 초기화
arr = [0] * 12
arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in range(4, max_n+1):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

for elem in data:
    print(arr[elem])