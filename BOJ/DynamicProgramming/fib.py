# 1003, 피보나치 함수
import sys
input = sys.stdin.readline

tc = int(input().rstrip())
data = []
for _ in range(tc):
    n = int(input().rstrip())
    data.append(n)

# 점화식에 활용할 배열 초기화
arr = [[0, 0] for _ in range(41)]
arr[0][0], arr[0][1] = 1, 0
arr[1][0], arr[1][1] = 0, 1

for i in range(2, max(data)+1):
    arr[i][0] = arr[i-1][0] + arr[i-2][0]
    arr[i][1] = arr[i-1][1] + arr[i-2][1]

for elem in data:
    print(arr[elem][0], arr[elem][1])