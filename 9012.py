"""
문제: 괄호가 올바르게 짝지어졌는지 YES or NO 결과를 출력
조건: 2 <= 괄호 문자열 <= 50

Reduction
1. 문자를 하나씩 체크한다.
2. 여는 문자면 스택에 넣고, 닫는 문자면 스택에서 꺼낸 문자와 비교한다.

시간/공간 복잡도
시간 복잡도: O(n)
공간 복잡도: O(n)

데이터 구조화
fixed capacity 스택

pseudo code
class Stack:
    def __init__(self, capacity):
        data 배열 초기화 [None] * capacity
        ptr 초기화 0
        capacity 초기화

    def push(self, value):
        만약 ptr이 capacity보다 크거나 같으면, return
        data[ptr]에 value 추가
        ptr 증가

    def pop(self):
        만약 ptr이 0이면, return -1
        pop_value = data[ptr]
        ptr 감소
        pop_value 반환

for 개행 반복:
    문자열을 배열로 변환
    is_right = True
    for 문자열 반복:
        '('이면 Stack에 push
        ')'이면 Stack에서 pop하고 '('인지 확인. 아니면 is_right = False
    is_right == True ? Yes, No 출력

edge case
((
)(
))
"""

import sys

N, *str_list = sys.stdin.read().strip().splitlines()


class Stack:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.ptr = 0
        self.capacity = capacity

    def push(self, value):
        if self.ptr >= self.capacity:
            return
        self.data[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.ptr <= 0:
            return -1
        self.ptr -= 1
        return self.data[self.ptr]


for line in str_list:
    is_right = True
    stack = Stack(len(line))
    for char in list(line):
        if char == "(":
            stack.push(char)
        else:
            pop_item = stack.pop()
            if pop_item == -1:
                is_right = False
    print("YES" if stack.ptr == 0 and is_right else "NO")
