"""
문제: 주어진 크기가 양수인 부분 수열 중에서 다 더한 값이 S가 되는 경우의 수는?
조건
1 <= 정수 개수 N <= 20
다 더한 값 | S | <= 100만


Reduction
1. dfs로 탐색한다.
2. 찾으면 카운트를 한다.


Pseudo Code

def dfs(idx, total, count):
    if S == total:
        return count + 1

    select_count = dfs(idx + 1, total + subsequence[idx], count)

    non_select_count = dfs(idx + 1, total, count)

    return select_count + non_select_count


print(dfs(0, 0, 0))


visited는 어떻게 적용하지?
"""

import sys

N, S, *subsequence = list(map(int, sys.stdin.read().strip().split()))


def dfs(idx, total):
    if idx == N:
        return 1 if S == total else 0

    return dfs(idx + 1, total + subsequence[idx]) + dfs(idx + 1, total)


print(dfs(0, 0) + (-1 if S == 0 else 0))
