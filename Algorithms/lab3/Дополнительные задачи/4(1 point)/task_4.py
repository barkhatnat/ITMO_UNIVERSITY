import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()
input_file = open('input.txt')
vertices, edges = map(int, input_file.readline().split())
graph = {}
for i in range(edges):
    from_vertex, to_vertex = map(int, input_file.readline().split())
    if from_vertex not in graph.keys():
        graph[from_vertex] = []
    if to_vertex not in graph.keys():
        graph[to_vertex] = []
    graph[from_vertex].append(to_vertex)
while len(graph.keys()) != vertices:
    index = 1
    for i in range(1, len(graph.keys()) + 2):
        if i not in graph.keys():
            index = i
            break
    graph[index] = []
graph = dict(sorted(graph.items(), key=lambda x: x[0]))
graph = dict(sorted(graph.items(), key=lambda x: x[1], reverse=True))
order = []
pre = [0 for _ in range(vertices + 1)]
post = [0 for _ in range(vertices + 1)]
visited = [False for _ in range(vertices + 1)]
clock = 1


def explore(v):
    order.append(v)
    visited[v] = True
    global clock
    pre[v] = clock
    clock += 1
    for w in graph[v]:
        if not visited[w]:
            explore(w)
    post[v] = clock
    clock += 1


def DFS(graph):
    for v in graph.keys():
        if not visited[v]:
            explore(v)


DFS(graph)
node_and_post = list(zip(order, [post[i] for i in order]))
topological_order = [i[0] for i in sorted(node_and_post, reverse=True, key=lambda x: x[1])]
with open('output.txt', 'w') as output_file:
    print(*topological_order, file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
