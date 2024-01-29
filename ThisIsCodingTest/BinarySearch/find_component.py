# p197, 부품 찾기
# 이진탐색
import sys

def binary_search(arr, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

input = sys.stdin.readline

n = int(input().rstrip())
comp_list = list(map(int, input().rstrip().split()))

m = int(input().rstrip())
find_list = list(map(int, input().rstrip().split()))

# 이진 탐색 수행 전에는 반드시 정렬이 선행되어야 함
comp_list.sort()

for i in range(m):
    result = binary_search(comp_list, find_list[i], 0, n-1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")