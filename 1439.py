"""
문제: 최소 횟수로 연속된 문자를 뒤집어서 같은 숫자로 만들기
조건
숫자는 1 or 0
0 <= 문자열 S < 100만

Reduction
1. 어느 문자의 연속된 문자가 작은지 판단한다.
2. 연속된 문자를 뒤집는다.

필요한 것
연속된 문자별 count

Pseudo code
0 카운터 초기화
1 카운터 초기화
prevLiteral 이전 문자 초기화

문자열 순회:
    문자가 이전 문자와 다를 때
        0이면 0 카운터 ++
        1이면 1 카운터 ++

0 카운터가 1 카운터보다 더 작거나 같으면:
    print(0 카운터)
크면:
    print(1 카운터)
"""

import sys

arr = list(sys.stdin.readline().strip())

zero_counter = 0
one_counter = 0
prev_literal = ""

for literal in arr:
    if literal != prev_literal:
        if literal == "0":
            zero_counter += 1
        else:
            one_counter += 1
    prev_literal = literal

if zero_counter <= one_counter:
    print(zero_counter)
else:
    print(one_counter)
