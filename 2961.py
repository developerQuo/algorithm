"""
문제: 신맛의 곱셈 조합과 쓴맛의 덧셈 조합의 차가 가장 작은 조합을 구하라
조건
1 <= 재료 N개 <= 10
신맛 S: 곱셈
쓴맛 B: 덧셈
1 <= S, B <= 10억

Reduction
1. DFS로 모든 조합을 구한다.
2. 현재 원소를 넣을지 말지 모두 재귀를 태운다.
3. 마지막 원소까지 계산하면 최소 값을 비교한다.

Pseudo Code
arr = 이중 배열 인풋

min_val = maxsize

def dfs(index, sour_comb, bitter_comb):
    if index > N-1:
        min_val = min(sour_comb의 곱 - bitter_comb의 합, min_val)

    sour_comb.append(arr[index][0])
    bitter_comb.append(arr[index][1])
    dfs(index + 1, sour_comb, bitter_comb)

    sour_comb.pop()
    bitter_comb.pop()
    dfs(index + 1, sour_comb, bitter_comb)

dfs(0, [], [])

print(min_val)
"""

import sys
import math

N = int(sys.stdin.readline())
arr = [list(map(int, line.strip().split())) for line in sys.stdin.readlines()]

min_val = sys.maxsize


def dfs(index: int, sour_comb: list, bitter_comb: list):
    global min_val

    if index > N - 1:
        if not len(sour_comb):
            return
        min_val = min(abs(math.prod(sour_comb) - sum(bitter_comb)), min_val)
        return

    sour_comb.append(arr[index][0])
    bitter_comb.append(arr[index][1])
    dfs(index + 1, sour_comb, bitter_comb)

    sour_comb.pop()
    bitter_comb.pop()
    dfs(index + 1, sour_comb, bitter_comb)


dfs(0, [], [])

print(min_val)
