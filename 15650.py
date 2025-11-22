"""
문제: 오름차순으로 길이가 M인 수열을 모두 출력
조건
1 <= 길이 M <= 최대 수 N <= 8

Reduction
1. 낮은 수부터 M개만 dfs로 순회한다.
2. 탐색 가능 수를 +1해서 탐색 범위를 좁힌다.

Pseudo Code
N, M 초기화
path = []

def dfs(offset):
    길이가 M이면
        print(*path)
        return

    offset부터 N까지 nums 순회 -> index:
        path.append(index + 1)
        dfs(index + 1)
        path.pop()

dfs(첫번째 자리 선정 -> 0)
"""

import sys
from collections import deque

N, M = list(map(int, sys.stdin.read().split()))


queue = deque()
queue.append([])

while queue:
    path = queue.popleft()

    if len(path) == M:
        print(*path)
        continue

    offset = path[-1] if len(path) else 0

    for i in range(offset, N):
        queue.append(path + [i + 1])


# path = []


# def dfs(offset):
#     if len(path) == M:
#         print(*path)
#         return

#     for i in range(offset, N):
#         path.append(i + 1)
#         dfs(i + 1)
#         path.pop()


# dfs(0)
