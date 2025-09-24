"""
문제: 1번으로부터 감염되는 속도 구하기
조건: 0 < 컴퓨터 수 N <= 100

데이터 구조
인접 리스트 & 큐

Reduction
1. 무방향 인접리스트를 만든다.
2. bfs를 진행한다.
3. 감염된 컴퓨터를 카운트한다.

시간복잡도: O(n - 1)
공간복잡도: O(n)

Pseudo Code

class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.length = 0

    def __len__(self):
        return self.length

    def push(self, key):
        self.tail.next = Node(key)
        self.tail = self.tail.next
        self.length += 1

    def pop(self):
        pop_node = self.head.next
        self.head.next = self.head.next.next
        self.length -= 1
        return pop_node.key


값이 배열인 딕셔너리 기반 인접리스트를 만든다.
adj = {}
visited = {}

def bfs():
    count = 0
    queue = Queue()
    queue.push(1)

    while len(queue):
        curr_val = queue.pop()
        for next_val in adj[curr_val]:
            만약 방문한 노드가 아니라면:
                count += 1
                visited[curr_val] = True
                queue.push(next_val)

    return count

print(bfs())


Edge Case
2
1
1 2
"""

import sys

N, M, *edges_str = sys.stdin.read().strip().splitlines()
edges = [list(map(int, edge_str.strip().split())) for edge_str in edges_str]


class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None


class Queue:
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.length = 0

    def __len__(self):
        return self.length

    def push(self, key):
        self.tail.next = Node(key)
        self.tail = self.tail.next
        self.length += 1

    def pop(self):
        pop_node = self.head.next
        self.head.next = self.head.next.next
        self.length -= 1
        if not self.length:
            self.tail = self.head
        return pop_node.key


adj = {i: [] for i in range(1, int(N) + 1)}
visited = {}

for from_node, to_node in edges:
    adj[from_node].append(to_node)
    adj[to_node].append(from_node)

for i in range(1, int(N) + 1):
    visited[i] = False


def bfs():
    count = 0
    queue = Queue()
    queue.push(1)
    visited[1] = True

    while len(queue):
        curr_val = queue.pop()
        if adj.get(curr_val):
            for next_val in adj[curr_val]:
                if not visited[next_val]:
                    count += 1
                    visited[next_val] = True
                    queue.push(next_val)

    return count


print(bfs())
