"""
문제: N개의 숫자 중, M개의 숫자가 포함되어 있는지 체크
조건: 1 <= N <= 50만 / 1 <= M <= 50만

reduction
1. N개의 숫자를 퀵정렬한다.
2. M의 숫자로 N을 이분탐색한다.
3. 있으면 1, 없으면 0을 출력

시간복잡도: O(N log N)

pseudo code
def quick_sort(left, right):
    pivot = (left + right) // 2
    pl, pr = left, right

    while pl <= pr:
        while pl 값이 pivot보다 작으면 pl++
        while pr 값이 pivot보다 크면 pr--
        if pl <= pr:
            pl 값과 pr 값 교환
            pl++, pr--

    left가 pr 보다 작으면 quick_sort(left, pr)
    right가 pl 보다 크면 quick_sort(pl, right)

def binary_search(left, right):
    mid = (left + right) // 2
    target과 mid가 같으면, return 1
    right - left가 0보다 작거나 같으면, return 0

    target이 mid보다 작으면, binary_search(left, mid - 1)
    target이 mid보다 크면, binary_search(mid + 1, right)

quick_sort로 N_list 정렬
M_list 반복문 돌려서 binary_search 결과 출력
"""

import sys

N_str, N_str_list, M_str, M_str_list = sys.stdin.read().strip().splitlines()
N_list = list(map(int, N_str_list.split()))
M_list = map(int, M_str_list.split())


def quick_sort(left, right):
    # pivot을 값이 아닌 인덱스로 저장하여 값을 교환할 때 에러가 났음
    pivot = N_list[(left + right) // 2]
    pl, pr = left, right

    while pl <= pr:
        while N_list[pl] < pivot:
            pl += 1
        while pivot < N_list[pr]:
            pr -= 1
        if pl <= pr:
            N_list[pl], N_list[pr] = N_list[pr], N_list[pl]
            pl += 1
            pr -= 1

    if left < pr:
        quick_sort(left, pr)
    if pl < right:
        quick_sort(pl, right)


def binary_search(target, left, right):
    mid = (left + right) // 2
    if target == N_list[mid]:
        return 1
    if right - left <= 0:
        return 0

    if target < N_list[mid]:
        return binary_search(target, left, mid - 1)
    if N_list[mid] < target:
        return binary_search(target, mid + 1, right)


result = []

quick_sort(0, len(N_list) - 1)
for num in M_list:
    result.append(str(binary_search(num, 0, len(N_list) - 1)))

print(" ".join(result))
