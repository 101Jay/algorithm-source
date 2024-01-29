# p115, 왕실의 나이트
# 구현

import sys
input = sys.stdin.readline

init_pos = input().strip()
init_x, init_y = (ord(init_pos[0]) - ord('a'))+1, int(init_pos[1])

# ord : alphabet -> int
# chr : int -> alphabet
steps = [
    (-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (-1, -2), (1, 2), (-1, 2)
]

result = 0
for step in steps:
    move_x = init_x + step[0]
    move_y = init_y + step[1]

    if move_x >= 1 and move_x <= 8 and move_y >= 1 and move_y <= 8:
        result += 1

print(result)