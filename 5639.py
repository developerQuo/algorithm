"""
문제: 전위 순회한 결과를 보고, 트리의 후위 순회 결과를 구하라.
조건: 0 < 노드 키 값 < 10^6 / 0 < 노드 수 <= 10,000

Reduction
1. 전위 순회 결과로 트리를 생성한다.
2. 트리의 후위 순회 결과를 출력한다.

데이터 구조: 이진 검색 트리

시간복잡도: O(log N)
공간복잡도: O(N)

Pseudo Code
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Binary_Search_Tree:
    def add_node(self, node, curr_node):
        루트가 없으면 루트에 등록
        현재 노드보다 작고
            left가 있으면 add_node(node, curr_node.left) 호출
            없으면 curr_node.left = node
        크고
            right가 있으면 add_node(node, curr_node.right) 호출
            없으면 curr_node.right = node

    def postorder_traversal(self, node):
        if node.left: postorder_traversal(node.left)
        if node.right: postorder_traversal(node.right)
        print(node)

이진 검색 트리 초기화
입력 값을 트리의 add_node 메서드로 입력
트리의 후위순회를 호출

Edge Case
1
"""

import sys

sys.setrecursionlimit(100000)
keys = list(map(int, sys.stdin.read().strip().splitlines()))


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def add_node(self, node, curr_node):
        if not self.root:
            self.root = node
            return

        curr_node = self.root if not curr_node else curr_node

        if node.key < curr_node.key:
            if curr_node.left:
                self.add_node(node, curr_node.left)
            else:
                curr_node.left = node
        else:
            if curr_node.right:
                self.add_node(node, curr_node.right)
            else:
                curr_node.right = node

    def postorder_traversal(self, node):
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node.key)


bst = Binary_Search_Tree()
for key in keys:
    bst.add_node(Node(key), None)
bst.postorder_traversal(bst.root)
