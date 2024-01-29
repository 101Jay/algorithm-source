# p367, 정렬된 배열에서 특정 수의 개수 구하기
# 이진탐색

# O(logN)의 시간복잡도로 구현해야 함
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
size, target = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))

def find_x(arr, target, size):
    left_index = bisect_left(arr, target)
    right_index = bisect_right(arr, target)

    if left_index == size:
        return -1

    return right_index - left_index

print(find_x(array, target, size))