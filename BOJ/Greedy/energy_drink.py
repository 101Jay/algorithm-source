# BOJ 20115, 에너지 드링크

import sys

input = sys.stdin.readline
size = int(input().strip())

# split
drink_list = list(map(int, input().split()))
drink_list.sort()

result = drink_list.pop()

for drink in drink_list:
    result += drink / 2

print(result)