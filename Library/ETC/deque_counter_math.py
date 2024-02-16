import math
from collections import deque, Counter

# deque -> 아래 네 개 메서드의 복잡도 O(1)
data = deque([2, 3, 4])

# 가장 뒤에 5를 추가
data.append(5) # [2, 3, 4, 5]

# 가장 앞에 1을 추가
data.appendleft(1) # [1, 2, 3, 4, 5]

# 가장 뒤의 원소 제거
data.pop() # [1, 2, 3, 4]

# 가장 앞의 원소 제거
data.popleft() # [2, 3, 4]

# deque([2,3,4])를 리스트화
print(list(data))

###################################

# 리스트 안의 특정 원소의 개수를 찾는 Counter
counter = Counter(['red', 'blue', 'red', 'green', 'black', 'white'])

# 'blue'가 등장한 횟수 : 1
print(counter['blue'])

# 사전 자료형으로 변환 key : 각 원소, value : 원소의 등장 횟수
print(dict(counter)) # {'red': 2, 'blue': 1, 'green': 1, 'black': 1, 'white': 1}

###################################

# factorial 함수
print(math.factorial(5)) # 120

# 제곱근을 출력하는 sqrt 함수
print(math.sqrt(7)) # 2.6457513110645907

# 최대공약수를 구해주는 gcd 함수
print(math.gcd(21, 14)) # 7

# 파이(pi), 자연상수(e)
print(math.pi) # 3.141592653589793
print(math.e) # 2.718281828459045