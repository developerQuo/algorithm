"""
문제: n번째 피보나치 수를 구하라
조건: n <= 90

Reduction
1. n-1번째 수를 dp에서 찾고 없으면 구한다.
2. n-2번째 수를 dp에서 찾고 없으면 구한다.
3. 두 수를 합쳐서 dp에 기록하고 반환한다.

점화식: F(n) = F(n-1) + F(n-2)

시간복잡도: O(n)
공간복잡도: O(n)

* 시간복잡도는 전체 호출 횟수를 세기 때문에 n^2
* 공간복잡도는 동시에 필요한 메모리(호출 스택 깊이)만 보기 때문에 n

Pseudo Code

dp = [None] * (N + 1)

def fibonacci(n):
    if dp[n]: return dp[n]

    n이 1이면 1 반환
    n이 0이면 0 반환

    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(N)

Edge Case
0

1
"""

import sys

N = int(sys.stdin.readline())


dp = [None] * (N + 1)


def fibonacci(n):
    if dp[n]:
        return dp[n]

    if n < 2:
        return n

    dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dp[n]


print(fibonacci(N))
