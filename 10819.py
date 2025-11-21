"""
문제: 주어진 식에서 최대값을 구하라
조건
3 <= 정수 개수 N <= 8
-100 <= 정수 크기 <= 100

Reduction
1. DFS로 최대값을 구한다.
2. 백트래킹으로 다음 경우의 수를 모두 구한다.

Pseudo Code
N, nums 초기화

visited = [False] * N
max_num = sys.minsize

def calc(path):
    result = 0
    for j in path:
        if j < N - 1:
            result += abs(path[j] - path[j+1])
    return result

def dfs(path):
    if len(path) == N:
        max_num = max(max_num, calc(path))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(path + [nums[i]])
            visited[i] = False

dfs([])
print(max_num)
"""

import sys

N, *num_arr = list(map(int, sys.stdin.read().split()))
visited = [False] * N


def compute(path):
    result = 0
    for j in range(len(path)):
        if j < N - 1:
            result += abs(path[j] - path[j + 1])
    return result


def dfs(path, max_num):
    if len(path) == N:
        return max(max_num, compute(path))

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result = dfs(path + [num_arr[i]], max_num)
            max_num = max(max_num, result)
            visited[i] = False

    return max_num


print(dfs([], float("-inf")))
