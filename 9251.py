"""
문제: 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾아라.
조건: 0 < 문자열 N, M <= 1000

Reduction
1. LCS로 가장 긴 문자열을 구한다.

시간복잡도: O(N * M)

Pseudo Code
N * M 이차원 배열을 만든다.
첫 원소가 0부터 시작하는 N과 M의 개별 배열을 만든다.

M 순회:
    N 순회:
        m이 n과 같으면 [m-1][n-1] + 1을 이차원 배열에 저장한다.
        m이 n과 다르면 [m][n-1], [m-1][n] 중 더 큰 값을 선택해서 저장한다.

max_val = 0
subsequence = []
N 순회:
    M 순회:
        max_val보다 커지는 지점의 인덱스를 배열에 저장

부분 수열 길이 출력

Edge Case
A
A

A
B
"""

import sys

N_str, M_str = sys.stdin.read().strip().splitlines()

N = list("0" + N_str)
M = list("0" + M_str)
matrix = [[0] * len(N) for _ in range(len(M))]

for col in range(1, len(M)):
    for row in range(1, len(N)):
        if M[col] == N[row]:
            matrix[col][row] = matrix[col - 1][row - 1] + 1
        else:
            matrix[col][row] = max(matrix[col][row - 1], matrix[col - 1][row])

max_val = 0
subsequence = []
for row in range(1, len(N)):
    for col in range(1, len(M)):
        if matrix[col][row] > max_val:
            subsequence.append(row)
            max_val += 1

print(len(subsequence))
