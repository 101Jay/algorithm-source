# BOJ 11727, 2xn 타일링2
# 점화식 : An = An-1 + An-2 * 2
import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr = [0] * 1001
arr[1] = 1
arr[2] = 3
for i in range(3, n+1):
    arr[i] = arr[i-1] + arr[i-2] * 2

print(arr[n] % 10007)