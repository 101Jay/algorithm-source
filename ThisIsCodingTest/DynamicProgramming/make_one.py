# p217, 1로 만들기
import sys
input = sys.stdin.readline

x = int(input().rstrip())

arr = [-1] * (x+1)

arr[1] = 0

for i in range(2, x+1):
    target = 100000

    if i % 5 == 0:
        target = min(target, arr[i//5] + 1)

    if i % 3 == 0:
        target = min(target, arr[i//3] + 1)

    if i % 2 == 0:
        target = min(target, arr[i//2] + 1)

    arr[i] = min(target, arr[i-1] + 1)

print(arr[x])