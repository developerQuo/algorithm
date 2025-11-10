"""
문제: 예산 내 최대 구매 가능 선물 개수 구하기
조건
1 <= 선물 가격 n개 <= 10만
1 <= 예산 b <= 10억
0 <= 선물 개수 a <= n
2 <= 선물 가격 (짝수) <= 10억

a개의 선물은 반 값 할인

할인은 가장 높은 가격에?

6 26 2
4 6 2 10 8 12

2 => 24
4 => 20
6 => 14
8 => 6
10/2 => 1
12


6 23 1
4 6 2 12 8 14

2 => 21
4 => 17
6 => 11
8 => 3
12
14

할인을 언제 어디에 매겨야하나
시점: 더 이상 담을 수 없을 때
어디: 새로 들어올 가격 => 안되면 기존에 구매한 가격에 추가로

Reduction
1. 선물 가격을 오름차순으로 정렬
2. 앞에서부터 차례대로 구매
3. 더 이상 구매하지 못하면 할인

시간복잡도: O(n)
n개씩 구매를 하면서 더 이상 진행이 안될 때, 할인 쿠폰을 먹이면 터짐
n개에 대해서 매번 a번 반복되는게 아니기 때문에 괜찮음. a는 차감

Data Structure
- queue: 구매 물건 별도 관리

Pseudo code
price_arr = []
discount = [0 for _ in range(N)]
B = 숫자
A = 숫자
purchase_list = deque([])

price_arr.sort()

price_arr iter:
    # 일단 구매 목록에 넣기
    purchase_list.append(price)
    임시 예산에서 차감

    while 할쿠 있고 임시 예산 초과면:
        구매 목록에서 비싼 물건부터 차례대로 할쿠 먹임

    여전히 예산 초과면:
        구매목록 길이에서 1빼고 출력
        종료
    아니면:
        B를 임시 예산으로 변경

"""

import sys
from collections import deque

N, B, A = list(map(int, sys.stdin.readline().split()))
price_arr = list(map(int, sys.stdin.readline().split()))

discount = [0 for _ in range(N)]
purchase_list = deque([])

price_arr.sort()

discount_ptr = len(price_arr) - 1
for price in price_arr:
    # 일단 구매 목록에 넣기
    purchase_list.append(price)
    tmp_B = B - price

    while A and tmp_B < 0 and discount_ptr > -1:
        if discount_ptr > len(purchase_list) - 1:
            discount_ptr = len(purchase_list) - 1

        if not discount[len(purchase_list) - 1]:
            ptr = len(purchase_list) - 1
            tmp_B += purchase_list[ptr] - purchase_list[ptr] / 2
            discount[ptr] += 1
            A -= 1
            continue

        if discount[discount_ptr]:
            discount_ptr -= 1
        else:
            tmp_B += purchase_list[discount_ptr] - int(purchase_list[discount_ptr] / 2)
            discount[discount_ptr] += 1
            discount_ptr -= 1
            A -= 1

    B = tmp_B

    if tmp_B < 0:
        print(len(purchase_list) - 1)
        break


if B >= 0:
    print(len(purchase_list))
