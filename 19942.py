"""
문제: 최소한의 비용으로 영양분 기준을 맞추기
조건
3 <= 재료 개수 N <= 15
0 <= 최소 영양 기준 mp, mf, ms, mv <= 500
0 < mp + mf + ms + mv
0 <= 재료의 영양 p, f, s, v, c <= 500

Reduction
1. dfs로 재료들의 조합을 구한다.
2. 최소 비용과 재료 조합을 출력한다.

Pseudo Code
N 초기화
mp, mf, ms, mv 초기화
재료 배열 ingredients 초기화
선택된 재료 배열 curr_picks 초기화

min_cost = -1
min_cost_picks = []

def dfs(index):
    index가 N과 같아지면 종료

    만약 최소 영양 기준을 통과하면
        min_cost_picks이 있다면
            min_cost = 현재 픽 vs 기존 픽 -> 비용 최소값
            min_cost_picks 업데이트
        min_cost_picks이 없다면
            min_cost = 현재 픽 비용
            min_cost_picks = 현재 픽
        탐색 종료

    이번 차례 재료를 넣지 않고 다음으로 진행

    이번 차례 재료를 넣고 다음으로 진행

dfs(0)

print(min_cost)
print(*min_cost_picks)
"""

import sys

N_str, nutrition_standard_str, *ingredients_str = sys.stdin.read().splitlines()
N = int(N_str)
mp, mf, ms, mv = list(map(int, nutrition_standard_str.split()))
ingredients = [list(map(int, line.split())) for line in ingredients_str]
curr_picks = []
curr_indexes = []

min_cost = -1
min_cost_picks = []


def calc_picks():
    sum_p = 0
    sum_f = 0
    sum_s = 0
    sum_v = 0
    sum_c = 0

    for p, f, s, v, c in curr_picks:
        sum_p += p
        sum_f += f
        sum_s += s
        sum_v += v
        sum_c += c

    return [sum_p, sum_f, sum_s, sum_v, sum_c]


def is_min():
    global min_cost, min_cost_picks

    p, f, s, v, c = calc_picks()

    if p >= mp and f >= mf and s >= ms and v >= mv:
        if min_cost > c:
            min_cost = c
            min_cost_picks = [*curr_indexes]
        elif min_cost == c:
            if curr_indexes < min_cost_picks:
                min_cost_picks = [*curr_indexes]
        elif min_cost == -1:
            min_cost = c
            min_cost_picks = [*curr_indexes]


def dfs(index):

    is_min()

    if index == N:
        return

    curr_picks.append(ingredients[index])
    curr_indexes.append(index)
    dfs(index + 1)
    curr_indexes.pop()
    curr_picks.pop()

    dfs(index + 1)


dfs(0)

print(min_cost)
print(*[index + 1 for index in min_cost_picks])
