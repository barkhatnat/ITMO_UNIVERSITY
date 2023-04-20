import time
import tracemalloc


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def find(self, x, node):
        if node is None or node.data == x:
            return node
        elif x < node.data:
            return self.find(x, node.left)
        else:
            return self.find(x, node.right)

    def insert(self, data):
        found_parent = None
        c_node = self.root
        while c_node is not None:
            found_parent = c_node
            if data < c_node.data:
                c_node = c_node.left
            elif data > c_node.data:
                c_node = c_node.right
            else:
                return
        new = Node(data)
        if found_parent is None:
            self.root = new
            new.parent = None
        elif data < found_parent.data:
            found_parent.left = new
            new.parent = found_parent
        elif data > found_parent.data:
            found_parent.right = new
            new.parent = found_parent

    def inorder(self, node, list_of_values):
        if node.left is not None:
            self.inorder(node.left, list_of_values)
        if node.data is not None:
            list_of_values.append(node.data)
        if node.right is not None:
            self.inorder(node.right, list_of_values)
        return list_of_values


start_time = time.perf_counter()
tracemalloc.start()
tree = Tree()
input_file = open('input.txt')
commands = input_file.readlines()
with open('output.txt', 'w') as output_file:
    for command in commands:
        action, value = command.split()
        value = int(value)
        match action:
            case "+":
                tree.insert(value)
            case "?":
                all_numbers = tree.inorder(tree.root, [])
                print(all_numbers[value - 1], file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
