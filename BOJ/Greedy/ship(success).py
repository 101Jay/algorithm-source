# BOJ 1092, 배

import sys
input = sys.stdin.readline

crane_num = int(input())
crane = list(map(int, input().split()))
crane.sort(reverse=True)

box_num = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)

if(crane[0] < box[0]):
     print(-1)
else:
     min_trans = 0
     while box:
        min_trans += 1

        # N + M번 보게 됨
        save_point = 0
        for cr in crane:
            for i in range(save_point, len(box)):
                save_point = i
                if cr >= box[i]:
                    box.pop(i)
                    break

     print(min_trans)