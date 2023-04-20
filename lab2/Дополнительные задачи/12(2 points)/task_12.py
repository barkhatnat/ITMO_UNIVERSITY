import time
import tracemalloc


class TreeNode:
    def __init__(self, value=None):
        self.left_child = None
        self.right_child = None
        self.value = value

    def insert_left(self, value, parent):
        if parent.left_child is None:
            parent.left_child = TreeNode(value)

    def insert_right(self, value, parent):
        if parent.right_child is None:
            parent.right_child = TreeNode(value)

    def find(self, value):
        answer = None
        if self.value == value:
            answer = self
        else:
            if self.left_child is not None:
                answer = self.left_child.find(value)
            if answer is None and self.right_child is not None:
                answer = self.right_child.find(value)
        return answer

    def is_balanced(self, node, isBalanced=True):
        if node.value is None or not isBalanced:
            return 0, isBalanced, 0
        left_height, isBalanced, balance = self.is_balanced(node.left_child, isBalanced)
        right_height, isBalanced, balance = self.is_balanced(node.right_child, isBalanced)
        if abs(left_height - right_height) > 1:
            isBalanced = False
        return max(left_height, right_height) + 1, isBalanced, right_height - left_height


def create_tree(i):
    parent = tree.find(info[i][0])
    if parent:
        left_i = info[i][left]
        right_i = info[i][right]
        if left_i != 0:
            tree.insert_left(info[left_i][0], parent)
            create_tree(left_i)
        else:
            tree.insert_left(None, parent)
        if right_i != 0:
            tree.insert_right(info[right_i][0], parent)
            create_tree(right_i)
        else:
            tree.insert_right(None, parent)


start_time = time.perf_counter()
tracemalloc.start()
input_file = open('input.txt')
N = int(input_file.readline())
info = [N]
for node in range(N):
    K, L, R = map(int, input_file.readline().split())
    info.append([K, L, R])
tree = TreeNode(info[1][0])
left = 1
right = 2

create_tree(1)
with open('output.txt', 'w') as output_file:
    for i in range(1, N + 1):
        print(tree.is_balanced(tree.find(info[i][0]))[2], file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
