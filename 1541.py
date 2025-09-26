"""
문제: 주어진 식에 괄호를 쳐서 최소값을 만들어라.
조건: 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않는다.

Reduction
1. 숫자와 연산자 스택을 각각 만든다.
2. 숫자와 연산자를 pop하면서 '+' 연산자가 나오면 계산해서 숫자 스택에 넣는다.
3. '-' 연산자가 나오면 pop한 숫자를 음수로 바꾼다.

Pseudo Code
num_stack = deque([])
operator_stack = deque([])

num_str = ""
문자열을 리스트로 변경해서 반복:
    문자가 '+' or "-"이면:
        num_str을 숫자로 바꿔서 num_stack에 추가
        연산자를 operator_stack에 추가
        num_str을 빈문자열로 초기화
    숫자면:
        num_str에 추가

def calculator():
    연산자 스택에 원소가 있다면 반복:
        연산자 스택에서 연산자를 꺼낸다.
        연산자가 '+'이면:
            numstack.append(num_stack.pop() + num_stack.pop())
        연산자가 '-'이면:
            numstack.append(-num_stack.pop())

    num_stack.pop() 반환

calculator()
10

10-10-20
"""

import sys
from collections import deque

num_str_list = list(sys.stdin.readline().strip())

num_stack = deque([])
operator_stack = deque([])

num_str = ""

for i in range(len(num_str_list)):
    if num_str_list[i] in ["+", "-"]:
        num_stack.append(int(num_str))
        operator_stack.append(num_str_list[i])
        num_str = ""
    else:
        num_str += num_str_list[i]
else:
    num_stack.append(int(num_str))


def calculator():
    while operator_stack:
        operator = operator_stack.pop()
        if operator == "+":
            num_stack.append(num_stack.pop() + num_stack.pop())
        elif operator_stack and operator_stack[-1] == "-":
            num_stack.append(num_stack.pop() + num_stack.pop())
        else:
            num_stack.append(-num_stack.pop() + num_stack.pop())

    return num_stack.pop()


print(calculator())
