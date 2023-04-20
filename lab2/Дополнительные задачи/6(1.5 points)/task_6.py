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

    def preorder(self, list_of_values):
        if self.value is not None:
            list_of_values.append(self.value)
        if self.left_child is not None:
            self.left_child.preorder(list_of_values)
        if self.right_child is not None:
            self.right_child.preorder(list_of_values)
        return list_of_values

    def inorder(self, list_of_values):
        if self.left_child is not None:
            self.left_child.inorder(list_of_values)
        if self.value is not None:
            list_of_values.append(self.value)
        if self.right_child is not None:
            self.right_child.inorder(list_of_values)
        return list_of_values

    def postorder(self, list_of_values):
        if self.left_child is not None:
            self.left_child.postorder(list_of_values)
        if self.right_child is not None:
            self.right_child.postorder(list_of_values)
        if self.value is not None:
            list_of_values.append(self.value)
        return list_of_values

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

    create_tree(0)
    inorder = tree.inorder([])
    for i in range(len(inorder) - 1):
        if inorder[i] < inorder[i+1]:
            pass
        else:
            answer = "INCORRECT"
            break
    else:
        answer = "CORRECT"
else:
    answer = "INCORRECT"
with open('output.txt', 'w') as output_file:
    print(answer, file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()

