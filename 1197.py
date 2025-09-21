"""
문제: 그래프 간선의 가중치 합이 최소인 MST를 구하라.
조건: 1 <= 정점 수 V <= 1만 / 1 <= 간선 수 E <= 10만

Reduction
1. 간선들을 가중치에 따라 오름차순으로 정렬한다.
2. 순서대로 간선을 선택하되, 사이클이 형성된 곳은 제외한다.

Data Structure
Union & Find

시간복잡도: O(E)
공간복잡도: O(V)

Pseudo Code
간선들을 가중치 기준으로 오름차순 정렬한다.
parent 정보를 담는 배열을 만든다.

weighted_sum = 0

def find(vertex):
    tmp_vertex = vertex
    while 임시노드와 노드의 부모가 다르다면:
        임시노드를 노드의 부모로 대체
    노드의 부모를 임시노드로 변경
    조상인 임시 노드를 반환

def union(vertex1, vertex2):
    두 노드에 대해 조상 찾기
    두 노드의 조상이 동일하면 패쓰(이미 연결됨)
    아니라면
        더 작은 쪽을 부모로 선정
        가중치 합산

간선들에 대해 반복
    union(노드1, 노드2)

print(weighted_sum)


Edge Case
2 1
1 2 -10

비 연결 그래프
4 2
1 2 1
3 4 1

"""

import sys

meta, *edge_str_list = sys.stdin.read().splitlines()
N, E = list(map(int, meta.strip().split()))
edge_list = [list(map(int, edge_info.strip().split())) for edge_info in edge_str_list]

edge_list.sort(key=lambda edge: edge[2])
parents = [i for i in range(N + 1)]

weighted_sum = 0


def find_parent(vertex):
    tmp_vertex = vertex
    while tmp_vertex != parents[tmp_vertex]:
        tmp_vertex = parents[tmp_vertex]
    parents[vertex] = tmp_vertex
    return tmp_vertex


def union_vertices(vertex1, vertex2, weight):
    global weighted_sum
    v1_parent, v2_parent = find_parent(vertex1), find_parent(vertex2)
    if v1_parent != v2_parent:
        if v1_parent < v2_parent:
            parents[v2_parent] = v1_parent
        else:
            parents[v1_parent] = v2_parent
        weighted_sum += weight


for v1, v2, w in edge_list:
    union_vertices(v1, v2, w)


print(weighted_sum)
