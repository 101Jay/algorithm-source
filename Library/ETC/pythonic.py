# *(asterisk)를 활용한 리스트 압축 해제
data = ['hello', 'world', 'goodbye']
new_data = [*data, 'welcome', 'goodday']
print(*new_data)


# divmod를 활용한 몫과 나머지 구하기
print(*divmod(8,4))


# int() 함수를 활용한 진법 변환
# 주의) base 진법으로 표현할 수 없는 수가 인자로 들어오면 ValueError 발생
num = '222'
base = 3
answer = int(num, base)
print(answer) # 26


# string의 메서드를 활용한 좌측/가운데/우측 정렬
# string을 n만큼의 사이즈로 각각 정렬
str_data = 'helloworld'
n = 20
print(str_data.ljust(n)) # 좌측 정렬
print(str_data.center(n)) # 가운데 정렬
print(str_data.rjust(n)) # 우측 정렬


# 영어 알파벳 대소문자 활용하기
import string
print(string.ascii_letters) # 소문자-대문자 순으로 모두 출력
print(string.ascii_lowercase) # 소문자
print(string.ascii_uppercase) # 대문자
print(string.digits) # 0123456789
# 아래와 같은 방식도 가능
for i in range(ord('a'), ord('z') + 1):
    print(chr(i), end="")
print()


# zip 함수를 활용한 이차원 리스트 행과열 뒤집기
data_lst = [[1,2,3], [4,5,6],[7,8,9]]
# *(asterisk)를 활용해 data_lst의 각 원소(1차원 리스트)들을 압축 해제한 뒤,
# zip을 활용해 이들의 각 원소를 하나씩 순서대로 묶어주면 행과 열이 바뀜
rev_lst = list(map(list, zip(*data_lst)))
print(rev_lst)


# zip 함수와 dict 함수를 활용해 두 리스트를 dictionary로 만들기
data_1 = ["python", "C", "C++"]
data_2 = ["class 1", "class 2", "class 3"]
collect_data = dict(zip(data_2, data_1))
print(collect_data)


# zip 함수를 이용해 i번째 원소와 i+1번째 원소의 차 구하기
zip_lst = [54, 21, 33, 12, 56]
zip_answer = []
# 주의) zip 함수는 서로 길이가 다른 리스트가 인자로 주어지면, 짧은 쪽까지만 반복
for n1, n2 in zip(zip_lst, zip_lst[1:]):
    zip_answer.append(abs(n1 - n2))
print(zip_answer)


# join을 활용하여 문자열 합치기
# 이터러블 객체를 한 번에 합칠 수 있음
join_lst = ['1', '11', '111', '1111']
answer = ''.join(join_lst)
print(answer)


# Counter 객체를 활용해 원소의 출현 빈도 구하기
from collections import Counter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = Counter(my_list) # 각 원소를 key로, 출현 빈도를 value로 사전식으로 구성
print(dict(answer))


# int와 sqrt를 활용하여 해당 수가 제곱수인지 확인하기
import math
num = 16
if math.sqrt(num) == int(math.sqrt(num)):
    print(f"{num} is sqrt!")


# for-else문을 활용하여, for문에서 특정 조건에 의해 break를 하면 실행되지 않는 else문을 추가할 수 있음
# 즉, 아래와 같은 코드에서 10보다 큰 수가 있다면 해당 for문을 break하고, 이 경우 else문은 실행되지 않음
numbers = [1, 2, 3, 4, 5, 6, 7]
limit = 10
for number in numbers:
    if number > 10:
        print("over the limit!")
        break
else:
    print("not over the limit!")


# python의 초간단한 swaping 기법
a = 10
b = 12
a, b = b, a # a = 12, b = 10
print(a, b)


# with ~ as 구문을 활용한 파일 입출력
'''
with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))
'''