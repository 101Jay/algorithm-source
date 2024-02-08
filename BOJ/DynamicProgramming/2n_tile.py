# BOJ 11726, 2xn 타일링
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [-1] * (1001)

arr[1] = 1
arr[2] = 2

for i in range(3, n+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[n] % 10007)