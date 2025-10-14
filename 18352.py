"""
인접행렬을 만들어서
bfs로 푼다?

시간복잡도 때문에 인접 리스트로 만들어서
bfs로 푼다.


문제: 특정 도시에서 출발해서 최단 거리가 K인 도시들의 번호를 출력하라
조건
2 <= 도시 개수 N <= 30만
1 <= 간선 M <= 100만
1 <= 도시 번호 K <= 30만
1 <= 출발 도시 X <= N

reduction
1. 간선을 인접리스트로 구현한다.
2. 출발 도시를 작업 큐에 넣고 방문하지 않은 인접 도시들을 모두 대기 큐에 넣는다.
3. 대기 큐에 있는 도시들을 작업 큐로 옮기고 거리에 +1을 한다.
4. 거리가 k가 되면 도시의 수를 센다.

pseudo code
adjacent_list = [[] for _ in range(len(N + 1))]
도시 경로 순회:
    adjacent_list에 push
visited = [false] * (N + 1)

work_q = deque()
next_work_q = deque()
distance = 0
count = 0

work_q.leftappend(시작점)

while (work_q와 next_work_q가 있으면):
    distance += 1

    while (work_q가 있으면):
        node = work_q.pop()
        만약 distance와 K가 일치하면
            count += 1
        아니면
            노드에서 이동 가능한 경로를 next_work_q에 모두 넣는다.

    next_work_q를 work_q에 옮긴다.
"""

from collections import deque
import sys

N, M, K, X = list(map(int, sys.stdin.readline().strip().split()))
edges = [list(map(int, edge_str.strip().split())) for edge_str in sys.stdin.readlines()]

adjacent_list = [[] for _ in range(N + 1)]
for edge in edges:
    adjacent_list[edge[0]].append(edge[1])
visited = [False] * (N + 1)

work_q = deque()
next_work_q = deque()
distance = 1
print_list = []

work_q.append(X)
visited[X] = True

if K == 0:
    print(X)

else:
    while len(work_q) or len(next_work_q):
        while len(work_q):
            node = work_q.popleft()
            for next_node in adjacent_list[node]:
                if not visited[next_node] and distance == K:
                    print_list.append(next_node)
                elif not visited[next_node]:
                    next_work_q.append(next_node)
                visited[next_node] = True
        if distance == K:
            break

        work_q.extend(next_work_q)
        next_work_q.clear()
        distance += 1

    if len(print_list):
        print_list.sort()
        for node in print_list:
            print(node)
    else:
        print(-1)
