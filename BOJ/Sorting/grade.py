# BOJ 10825, 국영수
import sys
input = sys.stdin.readline

num = int(input().rstrip())
arr = []
for _ in range(num):
    student = input().rstrip().split()
    arr.append((student[0], int(student[1]), int(student[2]), int(student[3])))

arr.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(num):
    print(arr[i][0])