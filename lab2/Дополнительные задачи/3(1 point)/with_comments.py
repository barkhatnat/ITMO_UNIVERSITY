class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        parent = None  # у корня нет родителей
        node = self.root  # сначала смотрим корень
        while node is not None:  # проверка на то, существует ли узел
            parent = node  # выбранный узел (при первом проходе корневой) является родителем для нового инсерта
            if key < node.key:
                node = node.left  # берем левый как следующий
            elif key > node.key:
                node = node.right  # берем правый как следующий
            else:
                return  # такой уже есть
        # вышли из цикла так как уткнулись в лист (нет определенных детей). значит сюда надо втыкать. parent содержит узел, к которому привяжем инсерт
        new = Node(key)  # создаем новый узел с новым значением
        if parent is None:  # если мы не нашли родилеля из листов, значит у нас нет ничего, значит мы создаем вершину (а у вершин нет родителей)
            self.root = new  # теперь значение корня это инсерт
        elif key < parent.key:
            parent.left = new  # создаем левого ребенка нашему листу
        elif key > parent.key:
            parent.right = new  # создаем правого ребенка листу

    def min(self, x):
        if self.root is None:  # если дерева нет, то 0
            return 0
        way = []
        node = self.root  # текущий узел
        while True:
            way.append(node)  # добавляем текущий узел в путь
            if x > node.key:  # если х больше текущего
                if node.right is None:  # если у текущего нет значения больше
                    break  # ну конец, больше некуда
                node = node.right  # идем дальше и берем значение больше
            elif x < node.key:  # если х меньше текущего
                if node.left is None:  # если у текущего нет значения меньше
                    return node.key  # значит наименьший из наибольших это как раз текущий
                node = node.left  # ну а если есть то идем туда
            else:  # нашли такое же зачение
                if node.right is None:  # если некуда больше идти право, то выход
                    break
                node = node.right  # если есть то идем вправо
                while node.left is not None:  # максимально влево
                    node = node.left
                return node.key  # возвращаем то что нашли
        way.reverse()
        # print([i.key for i in way])
        for i in range(len(way)):
            if way[i].key > x:
                return way[i].key
        return 0


input_file = open('input.txt')
content = input_file.readlines()
tree = Tree()
for request in content:
    operation = request[0]
    value = int(request[2:-1])
    with open('output.txt', 'a') as output_file:
        if operation == "+":
            tree.insert(value)
        elif operation == ">":
            print(tree.min(value), file=output_file)
            print(tree.min(value))
