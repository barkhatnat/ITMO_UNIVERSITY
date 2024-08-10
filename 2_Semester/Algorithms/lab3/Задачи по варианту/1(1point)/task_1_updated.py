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
    graph[to_vertex].append(from_vertex)
u, v = map(int, input_file.readline().split())
visited = [False] * (vertices + 1)
order = []


def explore(v):
    order.append(v)
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            explore(w)


def DFS(graph, start):
    for v in list(graph.keys())[start - 1:]:
        if not visited[v]:
            explore(v)
    return order


with open('output.txt', 'w') as output_file:
    print(int(v in DFS(graph, u)), file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
