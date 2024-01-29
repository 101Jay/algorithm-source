# BOJ 1092, 배 (실패)

import sys
input = sys.stdin.readline

ship_num = int(input())
ship_size = list(map(int, input().split()))
ship_size.sort()

box_num = int(input())
box_size = list(map(int, input().split()))

box_size.sort()

if ship_size[ship_num - 1] < box_size[box_num - 1]:
     print(-1)
else:
    limit_lst = []
    for i, ship in enumerate(ship_size):
          limit_lst.append(0)
          for box in box_size:
               if box > ship:
                   break
               limit_lst[i] += 1

    comp_num = 0
    min_trans = 0
    for index, max_num in enumerate(limit_lst):
        for _ in range(max_num):
            min_trans += 1
            comp_num += (ship_num - index)
            if comp_num >= box_num:
                break
        
        if comp_num >= box_num:
                break
               
    print(min_trans)