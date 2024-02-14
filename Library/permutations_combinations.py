from itertools import permutations, combinations, product

data = ['A', 'B', 'C']

# 순서를 신경 쓰는 순열
# itertools.permutations object를 list로 만든 형태
permutaion_result = list(permutations(data, 3)) # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# 순서를 고려하지 않는 조합
combination_result = list(combinations(data, 3)) # [('A', 'B', 'C')]

# 각 원소를 중복해서 순열로 만드는 product
product_result = list(product(data, repeat=2)) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]