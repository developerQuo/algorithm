"""
문제: 1부터 N까지 M개 수열을 모두 출력하라
조건
1 <= 출력 길이 M <= N <= 8
출력은 오름차순
중복되는 수열은 출력하지 않는다.

Reduction
1. dfs로 낮은 수부터 탐색
2. 백트래킹으로 방문 처리
3. path의 길이가 N이면 출력

Pseudo Code
N, M 초기화
visited = [False] * N

def dfs(path):
    if len(path) == N:
        print(*path)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(path + [i + 1])
            visited[i] = False

dfs([])
"""

import sys

N, M = list(map(int, sys.stdin.read().strip().split()))
visited = [False] * N


def dfs(path):
    if len(path) == M:
        print(*path)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(path + [i + 1])
            visited[i] = False


dfs([])
