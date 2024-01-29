# p180, 성적이 낮은 순서로 학생 출력하기 (계수 정렬)

import sys
input = sys.stdin.readline

size = int(input().rstrip())
grade_lst = []
for i in range(size):
    name, grade = input().rstrip().split()
    grade_lst.append((name, int(grade)))

grade_lst.sort(key=lambda x : x[1])

for i in range(size):
    print(grade_lst[i][0], end=" ")