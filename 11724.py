"""
문제: 방향 없는 그래프의 연결 요소 개수 구하기
조건: 1 <= 정점 개수 N <= 1000 / 0 <= 간선 개수 M <= N * (N - 1) / 2

Reduction
1. 새로운 입력 값을 set 배열에 담는다.
2. 기존에 있는 set 배열과 교차하는 곳이 있으면 합친다.
3. 없으면 배열에 추가한다.
4. 배열에 있는 set간에 한번 더 비교해서 합친다.

시간복잡도: O(N^2)
공간복잡도: O(N)

데이터 구조
set

Pseudo Code
class CC_Set:
    def __init__(self):
        self.set_arr = []

    def add_node(self, edge):
        new_edge_set = set(edge)
        for edge_set in self.set_arr:
            edge_set과 edge가 교차하면 edge_set에 합치기
            아니면 배열에 새로 추가

    def check_intersection(self):
        for pl in range(len(self.set_arr)):
            for pr in range(len(self.set_arr) - 1, pl, -1):
                pl_set과 pr_set이 교차하면 pl_set에 합치기

    def length(self):
        return len(self.set_arr)

cc_set = CC_Set()
입력 값을 add_node로 객체에 넣기
check_intersection으로 합칠 수 있는 부분 합치기
print(cc_set.length())

Edge Case
고립된 노드
"""

import sys

edge_meta, *edge_str_list = sys.stdin.read().splitlines()

N, M = list(map(int, edge_meta.strip().split()))


class CC_Set:
    def __init__(self):
        self.set_arr = []

    def add_node(self, edge):
        if not self.set_arr:
            self.set_arr.append(edge)
            return

        for i in range(len(self.set_arr)):
            if self.set_arr[i].intersection(edge):
                self.set_arr[i] = self.set_arr[i].union(edge)
                break
        else:
            self.set_arr.append(edge)

    def check_intersection(self):
        for pl in range(len(self.set_arr)):
            for pr in range(len(self.set_arr) - 1, pl, -1):
                if self.set_arr[pl].intersection(self.set_arr[pr]):
                    self.set_arr[pl] = self.set_arr[pl].union(self.set_arr[pr])
                    self.set_arr.remove(self.set_arr[pr])

    def length(self):
        sum_edge_node = set()
        for nodes in self.set_arr:
            sum_edge_node = sum_edge_node | nodes
        isolated_nodes_count = N - len(sum_edge_node)
        return isolated_nodes_count + len(self.set_arr)


cc_set = CC_Set()
for edge_str in edge_str_list:
    cc_set.add_node(set(map(int, edge_str.strip().split())))
cc_set.check_intersection()
print(cc_set.length())
