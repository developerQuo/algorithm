"""
문제: 배열에 값을 넣고, 가장 큰 값을 pop하기
조건
1 <= 연산 개수 N <= 10만 / 0 <= x < 2^31

Reduction
1. x > 0 일 때, 배열에 x를 추가한다.
2. 힙 정렬을 한다.
3. x == 0 일 때, 가장 큰 수를 pop 한다.

시간복잡도: O(N log N)
공간복잡도: O(N)

데이터 구조화
이진트리로 구성하고 힙 정렬로 최대값을 앞으로 유지

pseudo code
def heap_sort(sequence):
    def down_heap(root, last_leaf):
        largest = root

        left = root * 2 + 1
        right = left + 1
        largest가 last_leaf보다 같거나 작고, left보다 작으면 교환
        largest가 last_leaf보다 같거나 작고, right보다 작으면 교환
        largest가 가장 크면 종료


    max-heap 만들기 range((n-1)//2, -1, -1)
        down_heap()

    가장 아래 마지막 값부터 정렬 range(n-1, 0, -1)
        루트와 마지막 leaf 교환
        down_heap()



edge case
뭐가 있지?

힙 정렬
최대 힙 빌드: 마지막 부모 인덱스부터 루트까지 진행. i번 진행.
정렬: 루트(최대값)부터 마지막 leaf 교환을 반복. 빠진 루트는 최정렬에서 제외해나감.
"""

import sys

N, *nums = list(map(int, sys.stdin.read().split()))


heap_arr = []


def heap_sort(sequence):
    def down_heap(root, last_leaf):
        while True:
            largest = root
            left = largest * 2 + 1
            right = left + 1
            if left <= last_leaf and sequence[largest] < sequence[left]:
                largest = left
            if right <= last_leaf and sequence[largest] < sequence[right]:
                largest = right
            if largest == root:
                break

            sequence[root], sequence[largest] = sequence[largest], sequence[root]
            root = largest

    last_index = len(sequence) - 1

    for i in range(last_index // 2, -1, -1):
        down_heap(i, last_index)

    for i in range(last_index, 0, -1):
        sequence[0], sequence[i] = sequence[i], sequence[0]
        down_heap(0, i - 1)


for num in nums:
    if num > 0:
        heap_arr.append(num)
        heap_sort(heap_arr)
    else:
        if heap_arr:
            print(heap_arr[-1])
            heap_arr = heap_arr[:-1]
        else:
            print(0)
