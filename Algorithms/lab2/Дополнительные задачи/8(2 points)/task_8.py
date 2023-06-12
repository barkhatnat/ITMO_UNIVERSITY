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
    def inorder(self, list_of_values):
        if self.left_child is not None:
            self.left_child.inorder(list_of_values)
        if self.value is not None:
            list_of_values.append(self.value)
        if self.right_child is not None:
            self.right_child.inorder(list_of_values)
        return list_of_values

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

    def height(self):
        if self.value is None:
            return 0
        return 1 + max(self.left_child.height(), self.right_child.height())


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
print(tree.inorder([]))
with open('output.txt', 'w') as output_file:
    print(tree.height(), file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
