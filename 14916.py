"""
문제: 동전의 개수가 최소
조건: 1 <= 거스름돈 n <= 100,000

Reduction
1. 5로 거스름돈의 나머지를 구한다.
2. 나머지가 2로 나눠지지 않으면 5의 몫에서 -1을 해서 나머지를 다시 구한다.
3. 5의 몫과 2의 몫을 출력한다.

Pesudo Code
N = int(input())

N을 5로 나눈 나머지가 짝수가 아니면:
    5보다 클 때:
        5의 몫은 N // 5 - 1
    거스름돈은 N % 5 + 5
    2보다 클 때:
        2의 몫은 (N % 5 + 5) // 2
나머지가 홀수면:
    5보다 클 때:
        5의 몫은 N // 5
    거스름돈은 N % 5
    2보다 클 때:
        2의 몫은 (N % 5) // 2

거스름돈이 남으면 -1 출력

5의 몫 + 2의 몫을 출력

Edge Case
1
=> -1

2
=> 1

5
=> 1

3
=> -1
NOTE: 제일 큰 수보다 작은 수들에 대해 확인 필요
"""

import sys

N = int(sys.stdin.readline())
five, two = 0, 0

# 홀수
if N % 5 % 2:
    if N >= 5:
        five = N // 5 - 1
    change = N % 5 + 5
    if N >= 2 and N != 3:
        two = change // 2
        change = change % 2
# 짝수
else:
    if N >= 5:
        five = N // 5
    change = N % 5
    if N >= 2:
        two = change // 2
        change = change % 2

if change:
    print(-1)
else:
    print(five + two)

# TODO: 그리디로 풀면 수식 만들어서 증명하기
# TODO: dp로 풀어보기
