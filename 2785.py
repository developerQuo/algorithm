"""
문제: N개의 체인을 하나로 만들 수 있는 열고 닫을 최소한의 고리 수 구하기
조건:
2 <= 체인 개수 N <= 50만
1 <= 체인의 길이 L <= 100만
고리는 최대 2개의 인접한 고리 가짐

왜 정렬 문제인지 파악하기
=> 큰 거부터 연결해 나가면 되나? 그럼 최소 고리 보장? 젤 작은거를 하나씩 떼서 고리로 사용
OOO OOO
OOCOOO

0 0 0
0C0


왜 예제 3의 출력이 2가 아니지?
=> 1개 짜리 체인이 아니면 한 번 열면 양쪽 연결 가능
=> 그러면 왜 출력이 4가 아니지?
OOOO OOO OOOOO OOOOOOO OOOOOOOOO
OOOCOOO OOOOO OOOOOOO OOOOOOOOO
OOOCOOOCOOOO OOOOOOO OOOOOOOOO
OOOCOOOCOOOOCOOOOOO OOOOOOOOO
OOOCOOOCOOOOCOOOOOOCOOOOOOOO

OOO OOOO OOOOO OOOOOOO OOOOOOOOO
OO OOOOCOOOOO OOOOOOO OOOOOOOOO
O OOOOCOOOOOCOOOOOOO OOOOOOOOO
OOOOCOOOOOCOOOOOOOCOOOOOOOOO
=> 이러면 3개

4 3 5 7 9
3 4 5 7 9
2 4 5 17
1 4 23
0 28


시간복잡도: Nlog(N)

Reduction
1. 체인 길이 리스트를 오름차순 정렬
2. 가장 앞의 원소부터 1씩 차감하며 마지막 두 원소 합치기

Pseudo code
arr.sort()

ptr = 0
while (len(arr) - 1) - ptr > 1:
    arr[ptr]이 0이면:
        ptr += 1
    아니면:
        arr[ptr] -= 1
        arr[len(arr) - 1] = 뒤에 한 개 pop + 새로운 뒤에 한 개 + 1
"""

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort()

count = 0
ptr = 0
while len(arr) - 1 > ptr:
    if arr[ptr] == 0:
        ptr += 1
    else:
        last_num = arr.pop()
        arr[ptr] -= 1
        count += 1

print(count)
