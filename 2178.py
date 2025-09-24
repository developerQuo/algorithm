"""
문제: 최소 경로로 (1,1)에서 (N,M) 위치로 이동하라.
조건: 2 <= N, M <= 100

Reduction
1. 너비 우선으로 탐색한다.
2. 탐색한 칸은 1을 0으로 표시한다. (재방문 방지)

데이터 구조
큐

시간복잡도: O(N x M)
공간복잡도: O(N x M) x 2

Pseudo Code

class Node:
    def __init__(self, key):
        self.prev = None
        self.next = None
        self.key = key

class Queue:
    def __init__(self):
        self.front = 노드 생성
        self.rear = 노드 생성

    def push(self, key):
        key 노드 생성
        rear에 노드 추가
        rear의 prev의 next에 노드 추가
        새 노드의 prev에 기존 prev 노드 추가
        새 노드의 prev를 rear에 추가
        rear의 prev에 새 노드 추가

    def pop(self):
        front의 next를 pop 노드로 저장
        front의 next를 front의 next의 next로 저장
        front의 next의 next의 prev를 front로 저장
        return pop 노드

대기 큐 초기화
task 큐 초기화

def bfs():
    이동 카운트 초기화
    대기 큐와 task 큐가 빌 때까지 반복:
        카운트 ++
        task 큐가 빌 때까지 반복:
            pop 노드
            현재 위치가 N, M 위치인지 확인:
                도착했으면 count 출력하고 종료
            현재 위치를 1 -> 0 변경
            왼, 위, 오른, 아래 방향으로 1이 있는지 확인:
                있으면 대기 큐에 넣기
        대기 큐 작업을 task 큐에 옮기기


print(bfs())


Edge Case
2 2
11
11
"""

import sys

meta_str, *matrix_str = [line.strip() for line in sys.stdin.read().strip().splitlines()]
meta = meta_str.split()
N = int(meta[0])
M = int(meta[-1])
matrix = [list(line) for line in matrix_str]
max_col = len(matrix) - 1
max_row = len(matrix[0]) - 1

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Node:
    def __init__(self, key=None):
        self.prev = None
        self.next = None
        self.key = key


class Queue:
    def __init__(self):
        self.front = Node()
        self.rear = Node()
        self.length = 0

        self.front.next = self.rear
        self.rear.prev = self.front

    def push(self, key):
        node = Node(key)

        node.prev = self.rear.prev
        self.rear.prev.next = node
        node.next = self.rear
        self.rear.prev = node

        self.length += 1

    def pop(self) -> Node:
        pop_node = self.rear.prev
        pop_node.prev.next = self.rear
        self.rear.prev = pop_node.prev

        pop_node.prev = None
        pop_node.next = None

        self.length -= 1
        return pop_node


next_task_queue = Queue()
task_queue = Queue()


def bfs():
    count = 0

    while next_task_queue.length or task_queue.length:
        count += 1
        while task_queue.length:
            x, y = task_queue.pop().key
            if x == (M - 1) and y == (N - 1):
                return count

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= max_row and 0 <= ny <= max_col and matrix[ny][nx] == "1":
                    matrix[ny][nx] = "0"
                    next_task_queue.push((nx, ny))

        task_queue.front.next = next_task_queue.front.next
        task_queue.rear.prev = next_task_queue.rear.prev

        next_task_queue.front.next.prev = task_queue.front
        next_task_queue.rear.prev.next = task_queue.rear
        task_queue.length = next_task_queue.length

        next_task_queue.front.next = next_task_queue.rear
        next_task_queue.rear.prev = next_task_queue.front
        next_task_queue.length = 0


task_queue.push((0, 0))
matrix[0][0] = "0"
print(bfs())
