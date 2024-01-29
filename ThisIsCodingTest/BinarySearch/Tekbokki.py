# p201, 떡볶이 떡 만들기
# 이진탐색

import sys
input = sys.stdin.readline

def cut(lst, size):
    sum = 0
    for rice in lst:
        rest = rice - size
        if rest > 0:
            sum += rest
    return sum


num, size = map(int, input().rstrip().split())
rice_lst = list(map(int, input().rstrip().split()))

start, end = 0, max(rice_lst)
sum = 0
while start <= end:
    cut_size = (start + end) // 2
    sum = cut(rice_lst, cut_size)
    if sum == size :
        break
    elif sum > size:
        # sum이 더 크다는 것은, 조금 덜 잘라야 한다는 것
        start = cut_size + 1
    else:
        end = cut_size - 1

print(cut_size)