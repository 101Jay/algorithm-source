# p182, 두 배열의 원소 교체

import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
array_a = list(map(int, input().rstrip().split()))
array_b = list(map(int, input().rstrip().split()))

array_a.sort()
array_b.sort(reverse= True)

for i in range(k):
    if array_a[i] >= array_b[i]:
        break
    array_a[i], array_b[i] = array_b[i], array_a[i]

print(sum(array_a))
