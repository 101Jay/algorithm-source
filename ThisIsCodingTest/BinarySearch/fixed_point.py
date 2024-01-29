# p368, 고정점 찾기
# 이진탐색

import sys
input = sys.stdin.readline

size = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

def bi_search(start, end, arr):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1

    return None

# arr은 이미 정렬된 상태로 들어옴
start, end = 0, size - 1
result = bi_search(start, end, arr)

if result == None:
    print (-1)
else:
    print(result)