"""
문제: 최소 횟수로 연속된 문자를 뒤집어서 같은 숫자로 만들기
조건
숫자는 1 or 0
0 <= 문자열 S < 100만

Reduction
1. 문자열을 10진수로 바꿔서 2^n - 1 또는 0인지 확인한다.
2. 아니면 반으로 쪼갠다.
3. 앞 문자열의 마지막 문자와 뒤 문자열의 첫 문자가 같으면 합친다.
4. 더 이상 합칠 수 없으면 0, 1 카운터에 넣는다.

Data structure
- stack

Pseudo code
def iteration(literals: str):
    counter = [0, 0]
    stack에 문자열 넣기

    while(stack):
        literal = stack.pop()
        문자열을 10진수로 바꿨을 때, 결과가 0 or 2^(문자열 길이) - 1이면:
            0, 1 카운트++
        아니라면:
            prev = stack.push(literal[0, 길이 / 2의 몫])
            next = stack.push(literal[길이 / 2의 몫])
            prev의 마지막 문자와 next의 첫 문자가 같으면:
                0, 1 카운트--

    counter 중에 더 작은 것 출력
"""

import sys
from collections import deque

literals = sys.stdin.readline().strip()


counter = [0, 0]
stack = deque([literals])
leaf_arr = []

while stack:
    literal = stack.pop()
    if int(literal, 2) in (0, 2 ** len(literal) - 1):
        if literal[0] == "0":
            counter[0] += 1
        else:
            counter[1] += 1
        leaf_arr.append(literal)
    else:
        half = len(literal) // 2
        stack.append(literal[0:half])
        stack.append(literal[half:])

prev_literal = ""
for literal in leaf_arr:
    if not prev_literal:
        prev_literal = literal
        continue

    if literal[0] == prev_literal[-1]:
        if literal[0] == "0":
            counter[0] -= 1
        else:
            counter[1] -= 1
    prev_literal = literal


print(min(counter))
