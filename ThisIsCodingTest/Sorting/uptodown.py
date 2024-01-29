# p178, 위에서 아래로

# 계수 정렬 알고리즘 활용
import sys
input = sys.stdin.readline

size = int(input().rstrip())
count_lst = [0] * 100001

for i in range(size):
    count_lst[int(input().rstrip())] += 1

for i in range(1, 100001):
    for j in range(count_lst[-i]):
        print(100001 - i, end=" ")