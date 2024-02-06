# BOJ 9655, 돌 게임
import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr = [0] * 1001
arr[1] = "SK"
arr[2] = "CY"
arr[3] = "SK"

for i in range(4, n+1):
    if arr[i-1] == "SK":
        arr[i] = "CY"
    else:
        arr[i] = "SK"

print(arr[n])