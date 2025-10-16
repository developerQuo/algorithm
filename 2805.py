"""
최소값 0 - 최대값 높이를 준비
이분 탐색으로 가운데부터 잘라서 몇을 낼 수 있는지 본다.
출력 값이 크면 높이를 저장하고 더 진행해본다.
출력 값이 작으면 더 크게 찾는다.

문제: 필요한 나무 길이를 가질 수 있는 절단 최대 높이를 구하라.
조건
1 <= 나무 수 N <= 100만
1 <= 나무 길이 M <= 20억
0 <= 필요한 나무 높이 <= 10억

Reduction
1. 나무 높이의 반을 찍는다.
2. 얻을 수 있는 나무 길이를 계산한다.
3-1. 필요한 길이보다 크면 저장하고 1번부터 반복
3-2. 작으면 1번부터 반복

점화식
f(n) = f(n/2)

시간복잡도: O(logM) + O(N)

Pseudo Code
MAX_TREE_H = 최대 나무 길이 준비
나무를 길이로 정렬(내림차순)
max_cut_h = 0

def find_max_height(min_tree_h, max_tree_h):
    half = 나무 길이 중간값
    get_h = 0

    나무 수만큼 반복:
        half보다 작으면 break
        get_h += 나무 길이 - half

    필요한 길이가 get_h와 같으면
        max_cut_h = get_h
    크면
        max_cut_h = get_h
        find_max_height(min_tree_h, half)
    작으면
        find_max_height(half, max_tree_h)

find_max_height(0, MAX_TREE_H)
print(max_cut_h)
"""

import sys

N, M = list(map(int, sys.stdin.readline().split()))
TREE_LIST = list(map(int, sys.stdin.readline().split()))

TREE_LIST.sort(reverse=True)
MAX_TREE_H = TREE_LIST[0]
max_cut_h = 0


def find_max_height(min_tree_h, max_tree_h):
    global max_cut_h
    half = (max_tree_h + min_tree_h) // 2
    total_h = 0

    for tree_h in TREE_LIST:
        if tree_h < half:
            break
        total_h += tree_h - half

    if M == total_h:
        max_cut_h = half
    elif M > total_h:
        max_cut_h = half
        find_max_height(min_tree_h, half)
    else:
        find_max_height(half, max_tree_h)


find_max_height(0, MAX_TREE_H)
print(max_cut_h)
