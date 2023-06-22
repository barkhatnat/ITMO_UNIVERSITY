import time
import tracemalloc


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        parent = None
        c_node = self.root
        while c_node is not None:
            parent = c_node
            if data < c_node.data:
                c_node = c_node.left
            elif data > c_node.data:
                c_node = c_node.right
            else:
                return
        new = Node(data)
        if parent is None:
            self.root = new
        elif data < parent.data:
            parent.left = new
        elif data > parent.data:
            parent.right = new

    def find_closest_greater_number(self, x):
        if self.root is None:
            return 0
        full_way = []
        c_node = self.root
        while True:
            full_way.append(c_node)
            if x > c_node.data:
                if c_node.right is None:
                    break
                c_node = c_node.right
            elif x < c_node.data:
                if c_node.left is None:
                    return c_node.data
                c_node = c_node.left
            else:
                if c_node.right is None:
                    break
                c_node = c_node.right
                while c_node.left is not None:
                    c_node = c_node.left
                return c_node.data
        for i in range(len(full_way) - 1, -1, -1):
            if full_way[i].data > x:
                return full_way[i].data
        return 0


start_time = time.perf_counter()
tracemalloc.start()

input_file = open('input.txt')
content = input_file.readlines()
tree = Tree()
for request in content:
    operation = request[0]
    data = int(request[2:-1])
    with open('output.txt', 'a') as output_file:
        if operation == "+":
            tree.insert(data)
        elif operation == ">":
            print(tree.find_closest_greater_number(data), file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
