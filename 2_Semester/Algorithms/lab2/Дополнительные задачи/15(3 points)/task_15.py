import time
import tracemalloc
import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def __nodes_of_level(self, node, level, list_of_values):
        if node is None:
            return False, list_of_values
        if level == 1:
            list_of_values.append(node.data)
            return True, list_of_values
        left, list_of_values = self.__nodes_of_level(node.left, level - 1, list_of_values)
        right, list_of_values = self.__nodes_of_level(node.right, level - 1, list_of_values)
        return left or right, list_of_values

    def bsf(self, node, list_of_values):
        level = 1
        while self.__nodes_of_level(node, level, list_of_values)[0]:
            level = level + 1
        return list_of_values

    def tree_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def tree_max(self, node):
        while node.right is not None:
            node = node.right
        return node

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

    def __del_leaf(self, node):
        if node.parent.left == node:
            node.parent.left = None
        elif node.parent.right == node:
            node.parent.right = None

    def __del_one_child(self, node):
        if node.parent.right == node:
            if node.left is None:
                node.parent.right = node.right
            elif node.right is None:
                node.parent.right = node.left
        elif node.parent.left == node:
            if node.left is None:
                node.parent.left = node.right
            elif node.right is None:
                node.parent.left = node.left

    def __del_two_children(self, node):
        new = self.tree_max(node.left)
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
        if not self.is_balanced(self.root, True)[1]:
            self.balancing(self.root)

    def is_balanced(self, node, isBalanced=True):
        if node is None or not isBalanced:
            return 0, isBalanced
        left_height, isBalanced = self.is_balanced(node.left, isBalanced)
        right_height, isBalanced = self.is_balanced(node.right, isBalanced)
        if abs(left_height - right_height) > 1:
            isBalanced = False
        return max(left_height, right_height) + 1, isBalanced

    def rotation_left(self, node):
        if node is not None:
            new_node = node.right
            node.right = new_node.left
            if new_node.left:
                new_node.left.parent = node
            new_node.left = node
            if node.parent is not None:
                if node.parent.data > node.data:
                    node.parent.left = new_node
                    new_node.parent = node.parent
                else:
                    node.parent.right = new_node
                    new_node.parent = node.parent
            else:
                self.root = new_node
                new_node.parent = None
            node.parent = new_node
            return new_node
        else:
            return node

    def rotation_right(self, node):
        if node is not None:
            new_node = node.left
            node.left = new_node.right
            if new_node.right:
                new_node.right.parent = node
            new_node.right = node
            if node.parent is not None:
                if node.parent.data > node.data:
                    node.parent.left = new_node
                    new_node.parent = node.parent
                else:
                    node.parent.right = new_node
                    new_node.parent = node.parent
            else:
                self.root = new_node
                new_node.parent = None
            node.parent = new_node
            return new_node
        else:
            return node

    #
    def balancing(self, node):
        if node is None:
            return
        h1 = tree.is_balanced(node.left, True)[0]
        h2 = tree.is_balanced(node.right, True)[0]
        if h1 - h2 > 1:
            if tree.is_balanced(node.left.left, True)[0] > tree.is_balanced(node.left.right, True)[0]:
                # print("small right")
                tree.rotation_right(node)
            else:
                # print("big right")
                tree.rotation_left(node.left)
                tree.rotation_right(node)
        elif h2 - h1 > 1:
            if tree.is_balanced(node.right.right, True)[0] > tree.is_balanced(node.right.left, True)[0]:
                # print("small left")
                tree.rotation_left(node)
            else:
                # print("big left")
                tree.rotation_right(node.right)
                tree.rotation_left(node)
        else:
            self.balancing(node.right)
            self.balancing(node.left)


start_time = time.perf_counter()
tracemalloc.start()
tree = Tree()
input_file = open('input.txt')
N = int(input_file.readline())
values = [None]
for i in range(N):
    K, L, R = map(int, input_file.readline().split())
    tree.insert(K)
    values.append(K)
tree.delete(int(input_file.readline()))
tree.balancing(tree.root)
bsf = tree.bsf(tree.root, [])
with open('output.txt', 'w') as output_file:
    print(N - 1, file=output_file)
    for i in bsf:
        val = tree.find(i, tree.root)
        if val.left:
            l_ch = val.left.data
            l_ch = bsf.index(l_ch)
        else:
            l_ch = -1
        if val.right:
            r_ch = val.right.data
            r_ch = bsf.index(r_ch)
        else:
            r_ch = -1
        print(val.data, l_ch + 1, r_ch + 1, file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
