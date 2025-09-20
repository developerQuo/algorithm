"""
문제: 방향 없는 그래프의 연결 요소 개수 구하기
조건: 1 <= 정점 개수 N <= 1000 / 0 <= 간선 개수 M <= N * (N - 1) / 2

Reduction
1. 노드들의 부모를 자신으로 설정한다.
2. 간선을 이용해 하나씩 합친다.

시간복잡도: O(N)
공간복잡도: O(M)

데이터 구조


Pseudo Code
parent = list(range(1, N + 1))

def find_parent(node):
    while node의 최상단 부모를 찾아서 리턴

def union(node1, node2):
    node1과 node2의 부모 찾기
    부모가 같으면 종료
    부모가 다르면 node2를 node1에 붙이기 (node2의 부모를 node1의 부모로 설정)

edge_list 반복
    union(node1, node2)


Edge Case
고립된 노드
"""

import sys

edge_meta, *edge_str_list = sys.stdin.read().splitlines()

N, M = list(map(int, edge_meta.strip().split()))


parent = list(range(N + 1))


def find_parent(node):
    while parent[node] != node:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return node


def union(node1, node2):
    node1_parent, node2_parent = find_parent(node1), find_parent(node2)
    if node1_parent != node2_parent:
        parent[node2_parent] = node1_parent


for edge_str in edge_str_list:
    node1, node2 = list(map(int, edge_str.strip().split()))
    union(node1, node2)

roots = {find_parent(i) for i in range(1, N + 1)}
print(len(roots))
