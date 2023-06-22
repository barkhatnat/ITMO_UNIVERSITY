from collections import defaultdict, deque
import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()
input_file = open('input.txt')
m = int(input_file.readline())
reactions = [input_file.readline() for _ in range(m)]
source = input_file.readline().strip()
target = input_file.readline().strip()


def set_graph(reactions):
    graph = defaultdict(list)
    for reaction in reactions:
        substance1, substance2 = reaction.split("->")
        graph[substance1.strip()].append(substance2.strip())
    return graph


def find_target(graph, source, target):
    visited = set()
    queue = deque()
    queue.append((source, 0))
    while queue:
        current, count = queue.popleft()
        if current == target:
            return count
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, count + 1))
    return -1


graph = set_graph(reactions)
min_reactions = find_target(graph, source, target)

with open("output.txt", "w") as file:
    file.write(str(min_reactions))

print(time.perf_counter() - t_start)
print(float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
