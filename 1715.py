"""
문제: 카드 묶음의 최소 비교 횟수 구하기
조건: 1 <= 카드 묶음 N <= 100,000

reduction
1. 모든 카드 묶음을 최소 힙에 넣는다.
2. 힙에서 가장 적은 카드 묶음 2개를 꺼내서 합친다.
3. 결과를 힙에 다시 넣는다.

데이터 구조화
최소 힙 트리의 루트를 꺼내 쓴다.

pseudo code
def MinHeap(sequence):
    def sort(root, last_leaf):
        무한 루프 반복:
            left = root * 2 + 1
            right = left + 1
            smallest = root
            left가 last_leaf보다 작거나 같고, left 값이 smallest 값보다 작으면, smallest = left
            right가 last_leaf보다 작거나 같고, right 값이 smallest 값보다 작으면, smallest = right
            smallest와 root가 같으면 종료
            smallest 값과 root 값을 교환
            root = smallest

    n = len(sequence)

    for i in range((n - 1) // 2, -1, -1):
        sort(i, n - 1)

    for i in range(n - 1, 0, -1):
        sort(i, n - 1)

count = 0

카드 횟수 만큼 반복:
    카드 정렬
    count = 기존 카운트 + 첫 번째 카드 leftpop

print(count)

** 두개씩 뽑아서 더하고 다시 힙 트리에 추가하기


edge case
n = 1일 떄, 출력은 0
n = 4일 때, 5/5/5/5의 출력은 30

힙 구조 생성 이유
무한 루프 반복 이유
왜 탑다운으로 힙 정렬을 하지?
"""

import sys, copy

N, *card_list = list(map(int, sys.stdin.read().splitlines()))


class min_heap:
    def __init__(self, sequence):
        self.sequence = sequence  # 배열 초기화

        n = len(sequence)
        for i in range((n - 1) // 2, -1, -1):  # 힙 트리 생성
            self.sort(i, n - 1)

    def sort(self, root, last_leaf):
        while True:  # 하위 트리도 전부 체크
            left = root * 2 + 1
            right = left + 1
            smallest = root  # 가장 작은 값 초기화

            # 왼쪽 leaf가 leaf 범위 내이고, 왼쪽 값이 가장 작은 값일 때
            if left <= last_leaf and self.sequence[left] < self.sequence[smallest]:
                smallest = left

            # 오른쪽 leaf가 leaf 범위 내이고, 오른쪽 값이 가장 작은 값일 때
            if right <= last_leaf and self.sequence[right] < self.sequence[smallest]:
                smallest = right

            if smallest == root:  # 가장 작은 값이 root일 때
                break

            # 가장 작은 값을 가진 노드와 root 노드 값을 교환
            self.sequence[smallest], self.sequence[root] = (
                self.sequence[root],
                self.sequence[smallest],
            )
            root = smallest  # 가장 작은 값을 가졌던 노드를 새로운 root로 변경

    def pop_smallest(self):
        if len(self.sequence) == 1:
            return self.sequence.pop()

        pop_card = self.sequence[0]  # 가장 작은 값인 root 값을 pop
        self.sequence[0] = self.sequence.pop()  # leaf를 새로운 root로 변경
        return pop_card

    def push(self, new_val):
        self.sequence.append(new_val)


min_heap_tree = min_heap(copy.deepcopy(card_list))  # 힙 트리 객체 생성

cumulative_count = 0

while len(min_heap_tree.sequence) > 1:
    pop_card1 = min_heap_tree.pop_smallest()  # 트리에서 가장 작은 값을 pop

    min_heap_tree.sort(0, len(min_heap_tree.sequence) - 1)  # 정렬

    pop_card2 = min_heap_tree.pop_smallest()  # 한번 더 pop

    new_card = pop_card1 + pop_card2  # 1번 pop과 2번 pop을 합하기

    min_heap_tree.push(new_card)  # 힙 트리에 추가
    # 새 노드를 루트와 교환
    (
        min_heap_tree.sequence[0],
        min_heap_tree.sequence[len(min_heap_tree.sequence) - 1],
    ) = (
        min_heap_tree.sequence[len(min_heap_tree.sequence) - 1],
        min_heap_tree.sequence[0],
    )

    min_heap_tree.sort(0, len(min_heap_tree.sequence) - 1)  # 정렬

    cumulative_count += new_card


print(cumulative_count)
