# p99, 1이 될 때까지 (효율성 증진)
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

cnt = 0
while n > 1:
    target = (n // k) * k
    cnt += n - target

    n = target // k
    if n > 0:
        # 나눈 몫이 0보다 더 클때만 나눈 행위가 유의미함으로, cnt를 1증가
        cnt += 1

print(cnt)

'''
17 4
answer : 3

25 5
answer : 2
'''