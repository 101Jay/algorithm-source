# p99, 1이 될 때까지
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

cnt = 0
while n > 1:
    cnt += 1
    if n % k == 0:
        n = n // k
    else:
        n -= 1

print(cnt)

'''
17 4
answer : 3

25 5
answer : 2
'''