"""
문제: 동전의 개수를 최소로 사용하여 K를 완성시켜라.
조건: 1 ≤ 동전 개수 N ≤ 10, 1 ≤ 목표 값 K ≤ 100,000,000

Reduction
1. 값이 큰 동전부터 목표 값을 차감해나가고 카운트한다.
2. 카운트를 출력한다.

시간복잡도: O(N)

Pseudo Code
def coin_changing(k):
    curr = k
    count = 0

    동전 종류를 마지막 인덱스부터 순회:
        동전 종류보다 현재 값이 작을 때까지:
            현재 값에서 차감
            count ++

        만약 curr 값이 0이면 종료

    count 반환

print(coin_changing(K))

Edge Case
1 1
1

1 1
5
"""

import sys

N, K, *coins = list(map(int, sys.stdin.read().strip().split()))


def coin_changing(k):
    curr = k
    count = 0

    for i in range(len(coins) - 1, -1, -1):
        while curr >= coins[i]:
            curr -= coins[i]
            count += 1
        if curr == 0:
            break

    return count


print(coin_changing(K))
