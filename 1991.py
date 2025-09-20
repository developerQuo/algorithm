"""
문제: 이진트리를 전위, 중위, 후위 순회한 결과를 출력
조건: 1 <= 노드 N <= 26 / 루트는 A / 자식 없으면 .

Reduction
1. 입력 값을 이진 트리로 만든다.
2. 전위 순회한다.
3. 중위 순회한다.
4. 후위 순회한다.

Data Structure
- left, right, value가 있는 노드 클래스
- root 노드를 가진 이진 트리

시간복잡도: O(N)
공간복잡도: O(N)

Pseudo Code
class Node:
    def __init__(self, value):
        value 초기화
        left 초기화
        right 초기화

class Binary_Tree:
    def __init__(self):
        root 초기화

    def 전위 순회:
        자신 출력
        left 있으면 재귀 호출
        right 있으면 재귀 호출

    def 중위 순회:
        left 있으면 재귀 호출
        자신 출력
        right 있으면 재귀 호출

    def 후위 순회:
        left 있으면 재귀 호출
        right 있으면 재귀 호출
        자신 출력

def make_tree():
    본인 노드를 생성한다.
    left 노드가 있으면 left에 make_tree(left 노드)로 재귀를 호출한다.
    right 노드가 있으면 right에 make_tree(right 노드)로 재귀를 호출한다.
    return 본인 노드

tree_dict = {}
for me, left, right in range(tree_list):
    tree_dict[me] = [left, right]

Binary_Tree(make_tree(tree_dict[me]))


Edge Case
1
A . .
"""

import sys

N, *tree_list = [line.strip().split() for line in sys.stdin.read().splitlines()]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_Tree:
    def __init__(self, root_node):
        self.root = root_node

    def preorder_traversal(self, output: list, node: Node):
        output.append(node.value)
        if node.left:
            self.preorder_traversal(output, node.left)
        if node.right:
            self.preorder_traversal(output, node.right)

    def inorder_traversal(self, output: list, node: Node):
        if node.left:
            self.inorder_traversal(output, node.left)
        output.append(node.value)
        if node.right:
            self.inorder_traversal(output, node.right)

    def postorder_traversal(self, output: list, node: Node):
        if node.left:
            self.postorder_traversal(output, node.left)
        if node.right:
            self.postorder_traversal(output, node.right)
        output.append(node.value)


def make_tree(current_val):
    me_node = Node(current_val)

    left_val = tree_dict[current_val][0]
    if left_val != ".":
        me_node.left = make_tree(left_val)

    right_val = tree_dict[current_val][1]
    if right_val != ".":
        me_node.right = make_tree(right_val)

    return me_node


tree_dict = {}
for me, left, right in tree_list:
    tree_dict[me] = [left, right]

tree = Binary_Tree(make_tree("A"))

preorder_list = []
tree.preorder_traversal(preorder_list, tree.root)
print("".join(preorder_list))

inorder_list = []
tree.inorder_traversal(inorder_list, tree.root)
print("".join(inorder_list))

postorder_list = []
tree.postorder_traversal(postorder_list, tree.root)
print("".join(postorder_list))
