"""
문제: 효율을 못 내는 치킨집을 폐업 시키고, 도시의 치킨 거리의 최소값을 출력하라
조건
N x N 행렬
0: 빈 칸
1: 집
2: 치킨집
r, c 좌표

치킨 거리: 집과 가장 가까운 치킨집 사이의 거리

2 <= 도시 크기 N <= 50
1 <= 살아남을 치킨집 수 M <= 치킨집 수 <= 13
1 <= 집 수 < 2N

Reduction
1. 현재 존재하는 치킨집 수 중에 M개를 선택한다.
2. M개의 치킨과 각 집에서 가장 가까운 거리를 모두 더한다.
3. 가장 짧은 거리를 출력한다.

조합 적용은 집을 선택할 때

Pseudo Code
chicken_pos_list 초기화
home_pos_list 초기화

current_chicken = []
total_min_distance = float(inf)

def get_distance():
    distance = 0
    for hr, hc in home_pos_list:
        min_distance = float(inf)
        for cr, cc in current_chicken:
            min_distance = min(min_distance, 새로운 최소값)
        distance += min_distance
    distance 반환


def chicken_dfs(chicken_index):

    if chicken_index == len(chicken_pos_list):
        종료

    if len(current_chicken) == M:
        전체 최소 거리 = min(기존 최소 거리, 집과의 거리 계산)

    current_chicken.append(다음 치킨집)
    dfs(chicken_index + 1)
    current_chicken.pop()

    dfs(chicken_index + 1)

dfs(0)
print(total_min_distance)
"""

import sys

metadata, *mapstr = sys.stdin.read().splitlines()
N, M = list(map(int, metadata.strip().split()))

chicken_pos_list = []
home_pos_list = []
city_map = [list(map(int, line.strip().split())) for line in mapstr]

for row in range(len(mapstr)):
    new_line = []
    for col in range(len(city_map[row])):
        int_info = int(city_map[row][col])
        new_line.append(int_info)
        if int_info == 2:
            chicken_pos_list.append((row, col))
        if int_info == 1:
            home_pos_list.append((row, col))

    city_map[row] = new_line

current_chicken = []


def get_distance():
    distance = 0
    for hr, hc in home_pos_list:
        min_distance = float("inf")
        for cr, cc in current_chicken:
            value = abs(hr - cr) + abs(hc - cc)
            min_distance = min(min_distance, value)
        distance += min_distance
    return distance


def chicken_dfs(chicken_index, total_min_distance):
    if len(current_chicken) == M:
        return min(total_min_distance, get_distance())

    if chicken_index == len(chicken_pos_list):
        return float("inf")

    current_chicken.append(chicken_pos_list[chicken_index])
    insert_result = chicken_dfs(chicken_index + 1, total_min_distance)
    current_chicken.pop()

    not_insert_result = chicken_dfs(chicken_index + 1, total_min_distance)
    return min(insert_result, not_insert_result)


print(chicken_dfs(0, float("inf")))
