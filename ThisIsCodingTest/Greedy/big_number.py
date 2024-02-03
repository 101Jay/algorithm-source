# p92, 큰 수의 법칙 (일반적인 크기 제한)
import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

arr.sort(reverse=True)

sum = 0
cnt = k
while m > 0:

    if cnt > 0:
        sum += arr[0]
        cnt -= 1
    else:
        # cnt가 0일 경우
        sum += arr[1]
        cnt = k
    m -= 1

print(sum)
