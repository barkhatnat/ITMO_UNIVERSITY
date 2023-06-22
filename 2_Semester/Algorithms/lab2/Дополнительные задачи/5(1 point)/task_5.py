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

    def preorder(self, list_of_values, node):
        if node.data is not None:
            list_of_values.append(node.data)
        if node.left is not None:
            self.preorder(list_of_values, node.left)
        if node.right is not None:
            self.preorder(list_of_values, node.right)
        return list_of_values

    def find(self, x, node):
        if node is None or node.data == x:
            return node
        elif x < node.data:
            return self.find(x, node.left)
        else:
            return self.find(x, node.right)

    def exists(self, x):
        return bool(self.find(x, self.root))

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

    def tree_min(self, node):
        while node.left is not None:
            node = node.left
        return node

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
        return "none"

    def find_closest_less_number(self, x):
        if self.root is None:
            return 0
        full_way = []
        c_node = self.root
        while True:
            full_way.append(c_node)
            if x < c_node.data:
                if c_node.left is None:
                    break
                c_node = c_node.left
            elif x > c_node.data:
                if c_node.right is None:
                    return c_node.data
                c_node = c_node.right
            else:
                if c_node.left is None:
                    break
                c_node = c_node.left
                while c_node.right is not None:
                    c_node = c_node.right
                return c_node.data
        for i in range(len(full_way) - 1, -1, -1):
            if full_way[i].data < x:
                return full_way[i].data
        return "none"

    def __del_leaf(self, node):
        if node.parent.left == node:
            node.parent.left = None
        elif node.parent.right == node:
            node.parent.right = None

    def __del_one_child(self, node):
        if node.parent.left == node:
            if node.left is None:
                node.parent.left = node.right
            elif node.right is None:
                node.parent.left = node.left
        elif node.parent.right == node:
            if node.left is None:
                node.parent.right = node.right
            elif node.right is None:
                node.parent.right = node.left

    def __del_two_children(self, node):
        new = self.tree_min(node.right)
        # if node.parent.left == node:
        #     node.parent.left = new
        # elif node.parent.right == node:
        #     node.parent.right = new
        node.data = new.data
        self.__del_one_child(new)

    def delete(self, x):
        node = self.find(x, self.root)
        if node:
            if node.right is None and node.left is None:
                self.__del_leaf(node)
            elif node.left is None or node.right is None:
                self.__del_one_child(node)
            else:
                self.__del_two_children(node)



start_time = time.perf_counter()
tracemalloc.start()
tree = Tree()
input_file = open('input.txt')
commands = input_file.readlines()
with open('output.txt', 'w') as output_file:
    for command in commands:
        action, value = command.split()
        value = int(value)
        # print(action, value)
        match action:
            case "insert":
                tree.insert(value)
            case "exists":
                if tree.exists(value):
                    print("true", file=output_file)
                else:
                    print("false", file=output_file)
            case "next":
                print(tree.find_closest_greater_number(value), file=output_file)
            case "prev":
                print(tree.find_closest_less_number(value), file=output_file)
            case "delete":
                tree.delete(value)

print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
