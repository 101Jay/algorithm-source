# BOJ 2828, 사과 담기 게임

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
apple_num = int(input().strip())

apple_pos = [input().strip() for _ in range(apple_num)]

startPos, endPos = 0, m-1
changeCnt = 0

for i in apple_pos:

    index = int(i) - 1
    changePos = 0
    # 끝 위치와 비교
    if(endPos < index):
        changePos = index - endPos
    elif(startPos > index):
        changePos = -(startPos - index) # 왼쪽으로 이동하기 위해 음수화
    
    startPos, endPos = startPos + changePos, endPos + changePos
    changeCnt += abs(changePos)

print(changeCnt)