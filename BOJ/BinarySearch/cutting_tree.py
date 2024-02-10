# BOJ 2805, 나무 자르기
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
arr.sort()

res = 0
start, end = 0, arr[n-1]

while start <= end:
    mid = (start + end) // 2

    result = 0
    for elem in arr:
        # arr[i]로의 접근은 그 자체로 다시 log(N)의 복잡도임으로 시간초과가 발생
        remainder = elem - mid
        if remainder > 0:
            result += remainder

    if result == m:
        res = mid
        break
    elif result > m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)