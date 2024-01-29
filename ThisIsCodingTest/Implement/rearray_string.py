# p322, 문자열 재정렬
# 구현

# Facebook Interview
import sys
input = sys.stdin.readline

input_data = input().rstrip()

# A : 60 ~ Z : 95
str_list = []
num_sum = 0
for ch in input_data:
    if ord(ch) >= 60:
        str_list.append(ord(ch))
    else:
        num_sum += int(ch)

str_list.sort()

result = ""
for ch in str_list:
    result += chr(ch)
result += str(num_sum)

print(result)

# input : K1KA5CB7
# answer: ABCKK13

# input : AJKDLSI412K4JSJ9D
# answer: ADDIJJJKKLSS20