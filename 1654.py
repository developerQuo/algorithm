"""
문제: K개의 랜선으로 동일한 크기의 N개의 랜선을 만들 수 있는 최대 길이를 구하기
조건
1 <= 사용할 랜선 N개 <= 1백만
1 <= 보유 랜선 K개 <= 1만
K <= N

N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다?
=> 더 많이 만들어도 됨

Reduction
1. k개 랜선의 합에서 N을 나눠서 최대 길이 후보를 만든다.
2. 최대 길이 후보에서 이분 탐색으로 N개의 랜선이 만들어지는지 확인한다.

시간복잡도: O(랜선 길이 10억..) => 이분 탐색 O(log 랜선길이 * k)
log(10억 x 10000)?

점화식: f(n) = f(logn) + sum(k) // N

Data structure
- 큐: (start, end)

Pseudo code
max_length = k개 랜선 길이 합 // N
queue.append((1, max_length))

while queue:
    start, end = queue.popleft()
    mid = (start + end) // 2

    count = 0
    k 순회:
        count += k 원소 // mid

    count가 N과 같으면:
        max_length = mid
    count가 N보다 크면:
        max_length = mid
        queue.append((mid, end))
    count가 N보다 작으면:
        queue.append((start, mid))

print(max_length)


반복이 무한루프에 빠지는 경우는 없나?
"""

import sys
from collections import deque

K, N = list(map(int, sys.stdin.readline().strip().split()))
K_LAN = list(map(int, sys.stdin.read().strip().splitlines()))

max_length = max(K_LAN)
start = 1
end = max_length

while start <= end:
    mid = (start + end) // 2

    count = 0
    for lan in K_LAN:
        count += lan // mid

    if count >= N:
        max_length = mid
        start = mid + 1
    else:
        end = mid - 1

print(max_length)
