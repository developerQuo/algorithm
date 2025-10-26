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

11101101

1110 1101

11 10 11 01

11 1 0 11 0 1

11 10 11 01
count 10 -> 2개
count 01 -> 2개

1110 1101
count 1110 -> 같으니까 그대로 2개 유지
count 1101 -> 다르니까 1개 추가해서 3개

11101101
count 11101101 -> 다르니까 1개 추가해서 4개



0001100

000 1100

000 11 00

000 1100
count 1100 -> 2개

0001100
count 0001100 -> 3개


11001100110011000001

1100110011 0011000001

11001 10011 00110 00001

11 001 10 011 00 110 00 001

11 0 01 10 0 11 00 1 10 00 0 01

11 0 0 1 1 0 0 11 00 1 1 0 00 0 0 1

11 0 01 10 0 11 00 1 10 00 0 01
01 -> 0: 1, 1: 1
10 -> 0: 2, 1: 2
10 -> 0: 3, 1: 3


Pseudo Code

0 카운터
1 카운터

def recur(str literals) -> str:
    문자열을 10진수로 바꿨을 때, 결과가 0 or 2^(문자열 길이) - 1이면:
        0, 1 카운트++
        문자열 반환
    아니라면:
        prev = recur(literals.slice(0, 길이 / 2의 몫))
        next = recur(literals.slice(길이 / 2의 몫)))
        prev의 마지막 문자와 next의 첫 문자가 같으면:
            0, 1 카운트--
        return prev + next

"""

import sys

literals = sys.stdin.readline().strip()

zero_counter = 0
one_counter = 0


def recur(literals: str) -> str:
    global zero_counter, one_counter
    if int(literals, 2) in (0, 2 ** len(literals) - 1):
        if literals[0] == "0":
            zero_counter += 1
        else:
            one_counter += 1
        return literals
    else:
        prev = recur(literals[0 : len(literals) // 2])
        next = recur(literals[len(literals) // 2 :])
        if prev[-1] == next[0]:
            if next[0] == "0":
                zero_counter -= 1
            else:
                one_counter -= 1
        return prev + next


recur(literals)

if zero_counter <= one_counter:
    print(zero_counter)
else:
    print(one_counter)
