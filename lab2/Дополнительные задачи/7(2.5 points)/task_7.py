import time
import tracemalloc


class TreeNode:
    def __init__(self, value=None):
        self.left_child = None
        self.right_child = None
        self.value = value
        self.isFound = False

    def insert_left(self, value, parent):
        if parent.left_child is None:
            parent.left_child = TreeNode(value)

    def insert_right(self, value, parent):
        if parent.right_child is None:
            parent.right_child = TreeNode(value)

    def find(self, value):
        answer = None
        if self.value == value and self.isFound == False:
            answer = self
            self.isFound = True
        else:
            if self.left_child is not None:
                answer = self.left_child.find(value)
            if answer is None and self.right_child is not None:
                answer = self.right_child.find(value)
        return answer

    def check_tree(self):
        if self is None:
            return True
        if self.left_child.value is not None:
            if self.value > self.left_child.value:
                left_branch = self.left_child.check_tree()
            else:
                return False
        else:
            left_branch = True
        if self.right_child.value is not None:
            if self.value <= self.right_child.value:
                right_branch = self.right_child.check_tree()
            else:
                return False
        else:
            right_branch = True
        return left_branch and right_branch


def create_tree(i):
    parent = tree.find(info[i][0])
    if parent:
        left_i = info[i][left]
        right_i = info[i][right]
        if left_i >= 0:
            tree.insert_left(info[left_i][0], parent)
            create_tree(left_i)
        else:
            tree.insert_left(None, parent)
        if right_i >= 0:
            tree.insert_right(info[right_i][0], parent)
            create_tree(right_i)
        else:
            tree.insert_right(None, parent)


start_time = time.perf_counter()
tracemalloc.start()
input_file = open('input.txt')
N = int(input_file.readline())
info = []
for node in range(N):
    K, L, R = map(int, input_file.readline().split())
    info.append([K, L, R])
if info:
    tree = TreeNode(info[0][0])
    left = 1
    right = 2
    create_tree(0)
    if tree.check_tree():
        answer = "CORRECT"
    else:
        answer = "INCORRECT"
else:
    answer = "INCORRECT"
with open('output.txt', 'w') as output_file:
    print(answer, file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
