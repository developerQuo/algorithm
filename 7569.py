"""
문제: 토마토가 모두 익는 최소 일수를 구하라
조건:
- 익는 방향: 위 / 아래 / 왼쪽 / 오른쪽 / 앞 / 뒤. 대각선 X. 토마토가 없는 칸도 존재.
- 2 <= 상자 가로 칸 M <= 100 / 2 <= 상자 세로 칸 N <= 100 / 1 <= 상자 수 H <= 100
- 익은 토마토: 1 / 안 익은 토마토: 0 / 빈 칸: -1

Reduction
1. 매 초 익은 토마토의 영향을 계산한다.
2. 다 익으면 초 시간을, 그럴 수 없다면 -1을 출력한다.

데이터 구조
3차원 인접행렬

시간복잡도:
공간복잡도: O(M * N * H)

Pseudo Code
대기 스택을 만든다.

인접행렬에 있는 1을 모두 실행 스택에 넣는다.
timer = 0
대기 스택과 실행스택이 모두 비워질 때까지 반복
    실행 스택이 모두 처리될 때까지 반복
        실행 스택에서 pop
        상, 하, 좌, 우, 전, 후로 0이 있으면 대기 스택에 넣는다.

    timer += 1
    대기 스택을 실행 스택에 옮긴다.

인접행렬에 0이 남아 있으면 -1, 없으면 timer를 출력한다.

Edge Case
2 2 1
-1 -1
-1 -1
=> 0

2 2 1
0 0
0 0
=> 0

2 2 1
1 1
1 1
=> 0
"""

import sys
import copy

meta_str, *matrix_str = sys.stdin.read().splitlines()
M, N, H = list(map(int, meta_str.split()))
direction = [
    (1, 0, 0),  # 우
    (-1, 0, 0),  # 좌
    (0, 1, 0),  # 전
    (0, -1, 0),  # 후
    (0, 0, 1),  # 상
    (0, 0, -1),  # 하
]

todo_stack = []
task_stack = []
matrix = []

for h_index in range(H):
    h_arr = []
    for l_index in range(N):
        l_arr = []
        w_arr = list(map(int, matrix_str[h_index * N + l_index].split()))
        for w_index in range(M):
            tomato = w_arr[w_index]
            if tomato == 1:
                task_stack.append((w_index, l_index, h_index))
            l_arr.append(tomato)
        h_arr.append(l_arr)
    matrix.append(h_arr)

timer = 0
while todo_stack or task_stack:
    while task_stack:
        curr = task_stack.pop()
        for dw, dl, dh in direction:
            next_tomato = (curr[0] + dw, curr[1] + dl, curr[2] + dh)
            if (
                next_tomato[0] < M
                and next_tomato[0] >= 0
                and next_tomato[1] < N
                and next_tomato[1] >= 0
                and next_tomato[2] < H
                and next_tomato[2] >= 0
                and matrix[next_tomato[2]][next_tomato[1]][next_tomato[0]] == 0
            ):
                matrix[next_tomato[2]][next_tomato[1]][next_tomato[0]] = 1
                todo_stack.append(next_tomato)

    if todo_stack:
        timer += 1
        task_stack = copy.copy(todo_stack)
        todo_stack.clear()

# 인접행렬에 0이 남아 있으면 -1, 없으면 timer를 출력한다.
flatten_list = [
    tomato for h_depth in matrix for l_depth in h_depth for tomato in l_depth
]
if 0 in flatten_list:
    print(-1)
else:
    print(timer)
