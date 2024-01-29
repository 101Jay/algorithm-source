# binary search를 쉽게 해주는 bisect 모듈
# binary search는 기본적으로 정렬된 배열에서 특정 원소를 찾을 때 효과적으로 사용 가능
# bisect_left(), bisect_right()
# -> O(logn)의 시간복잡도로 작동

from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 7]
target = 4

print(bisect_left(a, target))
print(bisect_right(a, target))

# left_value <= x <= right_value 인 x의 개수를 구하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    return right_index - left_index

lst = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(lst, 2, 8))