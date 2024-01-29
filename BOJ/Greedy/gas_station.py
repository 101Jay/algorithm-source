# BOJ 13305, 주유소

import sys
input = sys.stdin.readline

city_num = int(input().strip())
city_distance = list(map(int, input().split()))
gas_cost = list(map(int, input().split()))

min_cost = gas_cost[0]
total_cost = 0

for i in range(city_num):
    if(min_cost > gas_cost[i]):
        min_cost = gas_cost[i]

    total_cost += min_cost * city_distance[i]

    if(i+2 == city_num):
        break

print(total_cost)