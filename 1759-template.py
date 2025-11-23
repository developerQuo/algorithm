"""
문제:
조건
L은 뽑는 수
C는 전체 알파벳 수
3 <= L <= C <= 15

모음 최소 한 개, 자음 최소 두 개 포함

Reduction
1. 알파벳을 오름차순으로 정렬
2. dfs로 조건(L 길이 & 모음 최소 1개 포함)에 맞는 조합을 출력

Pseudo Code
L, C 초기화
alphabet 오름차순 정렬
comb = []

def dfs(offset):
    if len(comb) == L:
        print(*comb)
        return

    for i in range(offset, C):
        comb.append(alphabet[i])
        dfs(offset + 1)
        comb.pop()

dfs(0)
"""

import sys

L, C = list(map(int, sys.stdin.readline().split()))
alphabet = sys.stdin.readline().strip().split()
alphabet.sort()
comb = []
vowel = {"a", "e", "i", "o", "u"}


def dfs(offset):

    if len(comb) == L:
        v = len(vowel.intersection(set(comb)))
        c = L - v
        if v >= 1 and c >= 2:
            print("".join(comb))
        return

    for i in range(offset, C):
        comb.append(alphabet[i])
        dfs(i + 1)
        comb.pop()


dfs(0)
