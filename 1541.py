"""
문제: 주어진 식에 괄호를 쳐서 최소값을 만들어라.
조건: 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않는다.

Reduction
1. - 연산자를 기준으로 나눈다.
2. 각 원소를 모두 계산한다.
3. 첫째 원소에서 나머지를 모두 빼준다.


Pseudo Code

num_segments = [ list(segment) for segment in str.split('-')]
sum_nums = []

sum_segment = 0
num_segments 반복 -> nums:

    num_str = ""
    nums 반복 -> num:
        문자가 '+'이면:
            num_str을 숫자로 바꿔서 sum_segment에 합산
        숫자면:
            num_str에 추가
    else:
        num_str을 숫자로 바꿔서 sum_segment에 합산

    sum_nums.append(-sum_segment)

print(sum(sum_nums))

10

10-10-20

55-50-40+30+20-10+5
"""

import sys

num_str_list = sys.stdin.readline().strip()

segments = [list(segment) for segment in num_str_list.split("-")]
sum_nums = []

sum_local = 0

for i in range(len(segments)):
    num_str = ""
    for literal in segments[i]:
        if literal == "+":
            sum_local += int(num_str)
            num_str = ""
        else:
            num_str += literal
    else:
        sum_local += int(num_str)

    sum_nums.append(-sum_local if i != 0 else sum_local)
    sum_local = 0

print(sum(sum_nums))
