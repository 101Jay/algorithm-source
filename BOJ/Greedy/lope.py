# BOJ 2217, 로프

import sys

input = sys.stdin.readline

size = int(input())
lopeList = [int(input().strip()) for _ in range(size)]

lopeList.sort()


lmax = lopeList[0] * len(lopeList)

for i, lope in enumerate(lopeList):
    temp = lope * (len(lopeList) - i)
    if(temp > lmax) : 
        lmax = temp

print(lmax)