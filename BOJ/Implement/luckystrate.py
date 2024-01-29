# BOJ 18406, 럭키 스트레이트

import sys
input = sys.stdin.readline

input_str = input().rstrip()

half_len = int(len(input_str) / 2)
left_num = input_str[0:half_len]
right_num = input_str[half_len:len(input_str)]

left_sum = 0
for i in left_num:
    left_sum += int(i)

right_sum = 0
for i in right_num:
    right_sum += int(i)

if right_sum == left_sum:
    print("LUCKY")
else:
    print("READY")