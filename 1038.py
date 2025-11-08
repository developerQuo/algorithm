"""
문제: 0부터 시작해서 N번째 감소하는 수를 구하라
조건:
0 <= N < 1백만

0 1 2 3 4 5 6 7 8 9
10                              1
20 21                           2
30 31 32                        3
40 41 42 43                     4
...
100                             1
200 210                         2
300 310 320 321                 4
400 410 420 421 430 431 432     7

dp..?

두번째 자리수 = 두번째 자리수보다 1씩 작은 첫번째 자리수들의 합
세번째 자리수 = 세번째 자리수보다 1씩 작은 두번째 자리수들의 합

점화식
F(n) =

Reduction
1.



0부터 차례대로 순회
1자리 수라면 배열에 바로 넣기, 딕셔너리(dp) 넣기
2자리 수라면 딕셔너리에 수가 있으면 가져오기

Pseudo code
arr = []
dict = {}

arr_index = 0
curr = 0
while curr <= 1백만:
    for i in range(1, 10):
        arr_index가 N이면:
            출력
            break

        curr이 1자리 수면:
            dict[curr] = 1
        curr이 2자리 수 이상이면:
            curr의 각 자리 수 순회 => now:
                dict[curr] += dict[now]
            dict[curr] += 1

"""

"""
0 1 2 3 4 5 6 7 8 9

1 2 3 4 5 6 7 8 9

2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 9 10

3 4 5 6 7 8 9 10
3 4 5 6 7 8 9 10 20 21

4 5 6 7 8 9 10 20 21
4 5 6 7 8 9 10 20 21 30 31 32

5 6 7 8 9 10 20 21 30 31 32
5 6 7 8 9 10 20 21 30 31 32 40 41 42 43

Reduction
1. 큐에 0부터 9까지 담는다.
2. 하나씩 빼면서 카운트한다.
3. 0부터 pop 숫자의 마지막 자리의 숫자 범위까지, 뺀 숫자 뒤에 붙여서 큐에 넣는다.

시간복잡도: O(N)
공간복잡도: O(N)

Pseudo code
queue = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
count = 0
curr = -1

while (count <= N and queue):
    queue에서 pop
    count += 1
    curr = pop 숫자

    for num in range(0, pop 숫자 마지막 숫자):
        queue.append(curr 숫자문자 + num 숫자문자)

print(-1 if queue else curr)
"""
import sys
from collections import deque

N = int(sys.stdin.read())

queue = deque(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
count = -1
curr = "-1"

while count < N and queue:
    curr = queue.popleft()
    count += 1

    for num in range(0, int(curr[-1])):
        queue.append(curr + str(num))

print(-1 if count != N else curr)
