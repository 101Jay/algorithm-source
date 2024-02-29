# BOJ 2579, 계단 오르기
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    arr.append(int(input().rstrip()))

con_arr = [[0, 0]] * 301 # (An-2 max, An-1의 첫 번째 원소)
con_arr[1] = [arr[0], arr[0]]

for i in range(2, n+1):
    # 점화식 : An = (An-2 max, An-1의 첫 번째 원소)
    con_arr[i] = [max(con_arr[i-2]) + arr[i-1], con_arr[i-1][0] + arr[i-1]]

print(max(con_arr[n]))