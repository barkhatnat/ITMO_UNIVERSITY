import time
import tracemalloc


class TreeNode:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    @staticmethod
    def insert_left(data, parent):
        if parent.left is None:
            parent.left = TreeNode(data)

    @staticmethod
    def insert_right(data, parent):
        if parent.right is None:
            parent.right = TreeNode(data)

    def find(self, data):
        answer = None
        if self.data == data:
            answer = self
        else:
            if self.left is not None:
                answer = self.left.find(data)
            if answer is None and self.right is not None:
                answer = self.right.find(data)
        return answer

    def preorder(self, list_of_values):
        if self.data is not None:
            list_of_values.append(self.data)
        if self.left is not None:
            self.left.preorder(list_of_values)
        if self.right is not None:
            self.right.preorder(list_of_values)
        return list_of_values

    def inorder(self, list_of_values):
        if self.left is not None:
            self.left.inorder(list_of_values)
        if self.data is not None:
            list_of_values.append(self.data)
        if self.right is not None:
            self.right.inorder(list_of_values)
        return list_of_values

    def postorder(self, list_of_values):
        if self.left is not None:
            self.left.postorder(list_of_values)
        if self.right is not None:
            self.right.postorder(list_of_values)
        if self.data is not None:
            list_of_values.append(self.data)
        return list_of_values


start_time = time.perf_counter()
tracemalloc.start()
input_file = open('input.txt')
N = int(input_file.readline())
info = []
for node in range(N):
    K, L, R = map(int, input_file.readline().split())
    info.append([K, L, R])
tree = TreeNode(info[0][0])
left = 1
right = 2


def create_tree(node_index):
    parent = tree.find(info[node_index][0])
    if parent:
        left_index = info[node_index][left]
        right_index = info[node_index][right]
        if left_index >= 0:
            tree.insert_left(info[left_index][0], parent)
            create_tree(left_index)
        else:
            tree.insert_left(None, parent)
        if right_index >= 0:
            tree.insert_right(info[right_index][0], parent)
            create_tree(right_index)
        else:
            tree.insert_right(None, parent)


create_tree(0)
with open('output.txt', 'w') as output_file:
    print(*tree.inorder([]), file=output_file)
    print(*tree.preorder([]), file=output_file)
    print(*tree.postorder([]), file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
