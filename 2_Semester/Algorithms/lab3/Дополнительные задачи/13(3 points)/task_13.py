from collections import defaultdict
import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()
input_file = open('input.txt')
N, M = map(int, input_file.readline().split())
graph = defaultdict(list)
field = []
for i in range(N):
    line = input_file.readline().strip()
    line = [c for c in line]
    field.append(line)

# for line in field:
#     print(line, end='\n')

counter = 1
new_field = []
for i in range(N):
    new_field.append([0] * M)

for line in range(N):
    for square in range(M):
        if field[line][square] == "#":
            graph[counter] = []
            new_field[line][square] = counter
            counter += 1
        if field[line][square] == "#":
            if new_field[line][square - 1] and square > 0:
                graph[new_field[line][square - 1]].append(new_field[line][square])
                graph[new_field[line][square]].append(new_field[line][square - 1])
            if new_field[line - 1][square] and line > 0:
                graph[new_field[line - 1][square]].append(new_field[line][square])
                graph[new_field[line][square]].append(new_field[line - 1][square])
for line in new_field:
    print(line, end='\n')
visited = [False] * (len(graph.keys()) + 1)
order = []
CC_nums = [0] * (len(graph.keys()) + 1)
cc_number = 1


def explore(v):
    CC_nums[v] = cc_number
    order.append(v)
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            explore(w)


def DFS(graph, start):
    global cc_number
    for v in list(graph.keys())[start - 1:]:
        if not visited[v]:
            explore(v)
            cc_number += 1


DFS(graph, 1)
with open('output.txt', 'w') as output_file:
    print(max(CC_nums), file=output_file)
print(time.perf_counter() - t_start)
print(float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
