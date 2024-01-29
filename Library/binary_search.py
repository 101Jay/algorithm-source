import sys

def binary_search(array, target, start, end):

    # while문을 활용한 이진탐색 구현
    while start <= end:
        # 반내림으로 mid 결정
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

input = sys.stdin.readline
n, target = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))

# 이진 탐색은 정렬된 리스트로 진행
array.sort()


result = binary_search(array, target, 0, n-1)
if result == None:
    print("Can not find the element")
else:
    print("Index of the element:", result)