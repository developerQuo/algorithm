"""
문제: 암호 후보를 모두 구하라
조건:
암호 L은 최소 1개의 모음, 최소 2개의 자음으로 구성
오름차순
3 <= 암호 길이 L <= 문자 종류 C <= 15
1 <= 모음 <= 4
1 <= 자음 <= 14

각각의 문자는 한 번에 하나씩만 사용됨
자음을 몇 개 사용 가능한지만 계산하면 모음 조합을 갖다 붙이면 됨

문자: a, c, i, s, t, w

Reduction
1. 문자들을 오름차순으로 정렬한다.
2. dfs로 문자를 하나씩 꺼내서 다음 문자를 선택한다.
3. 길이가 L일 때, 모음 1이상, 자음 2이상 조건이 되면 출력한다.
4. 현재 꺼낸 문자의 선택을 취소
"""

import sys
from collections import deque

L, C = list(map(int, sys.stdin.readline().strip().split()))
chars = sys.stdin.readline().strip().split()
chars.sort()

vowels = ["a", "e", "i", "o", "u"]

password = deque()


def dfs(index, vowel_count, consonant_count):
    if len(password) == L:
        if vowel_count >= 1 and consonant_count >= 2:
            print("".join(password))
        return

    for i in range(index, C):
        c = chars[i]

        password.append(c)

        if c in vowels:
            dfs(i + 1, vowel_count + 1, consonant_count)
        else:
            dfs(i + 1, vowel_count, consonant_count + 1)

        password.pop()


dfs(0, 0, 0)
