# BOJ 20365, 블로그2
# 그리디

import sys
input = sys.stdin.readline

size = int(input())
t_str = list(input().strip())

# 모두 blue로 칠한 경우
b_str = ['B' for _ in range(size)]

b_change = 1
conCh = False
for i, ch in enumerate(b_str):
    if(ch != t_str[i]):
        # 바꿔줘야 함
        if(conCh == False):
           # 연속적이지 않을 때만 1더해줌
           b_change += 1
        
        conCh = True
    else:
        conCh = False

# 모두 red로 칠한 경우
r_str = ['R' for _ in range(size)]
r_change = 1
conCh = False
for i, ch in enumerate(r_str):
    if(ch != t_str[i]):
        # 바꿔줘야 함
        if(conCh == False):
           # 연속적이지 않을 때만 1더해줌
           r_change += 1
        
        conCh = True
    else:
        conCh = False

if(b_change > r_change): 
    result = r_change
else:
    result = b_change

print(result)