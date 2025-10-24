"""
문제: 목적지까지 최소 이동 시간을 구하라
조건
1 <= R <= 50, 1 <= C <= 50
. : 빈 곳
* : 물
X : 돌
D : 목적지
S : 시작점

물이 찰 예정인 칸으로 이동 불가
상하좌우로 매 분마다 물이 1칸씩 차고, 고슴도치도 1칸씩 이동
이동 불가라면 KAKTUS 출력

Reduction
1. 물이 찬다.
2. 고슴도치가 이동한다.
3. 만약 비버 굴에 도착하면 끝이 난다.

Data Structure
티떱숲 지도 & 방문기록: 인접행렬
이동순서: 큐

Pseudo Code
지도 2차원 인접행렬을 만든다. (방문: v)
queue를 초기화 (시작점 넣기)
timer = 0

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))

def visit_beaver():
    while(queue) {
        돌, 시작점, 도착점을 제외하고 상하좌우로 물을 채운다.

        비어있는 곳인 상하좌우로 고슴도치를 이동시킨다.
        이동한 곳을 v로 방문처리한다.

        만약 도착했으면 1을 반환한다.
    }

    return 0

print(timer)
"""

from collections import deque
import sys

C, R = list(map(int, sys.stdin.readline().strip().split()))
lines = sys.stdin.readlines()
S_pos = None
matrix = []
water = []
for c in range(C):
    row = []
    for r in range(R):
        row.append(lines[c][r])
        if lines[c][r] == "S":
            S_pos = (r, c)
        elif lines[c][r] == "*":
            water.append((r, c))
    matrix.append(row)
queue = deque()
queue.append(S_pos)
queue.extend(water)
next_queue = deque([])
timer = 0

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))


def visit_beaver():
    global timer
    while queue or next_queue:
        timer += 1
        while queue:
            r, c = queue.popleft()

            if matrix[c][r] == "v" or matrix[c][r] == "S":  # 고슴도치
                for dr, dc in direction:
                    sr, sc = r + dr, c + dc
                    if 0 <= sr < R and 0 <= sc < C:
                        if matrix[sc][sr] == "D":
                            return 1
                        elif matrix[sc][sr] == ".":
                            matrix[sc][sr] = "v"
                            next_queue.append((sr, sc))

            if matrix[c][r] == "*":  # 물
                for dr, dc in direction:
                    sr, sc = r + dr, c + dc
                    if 0 <= sr < R and 0 <= sc < C and matrix[sc][sr] in ("v", "."):
                        matrix[sc][sr] = "*"
                        next_queue.append((sr, sc))

        queue.extend(next_queue)
        next_queue.clear()

    return 0


if visit_beaver():
    print(timer)
else:
    print("KAKTUS")
