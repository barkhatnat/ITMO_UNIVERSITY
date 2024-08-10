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
queue = []
visited = [False] * (vertices + 1)
colors = ['white' for _ in range(vertices + 1)]


def dfs(start, visited, graph):
    visited[start] = True
    colors[start] = 'grey'
    for v in graph[start]:
        if colors[v] != 'grey':
            dfs(v, visited, graph)
        else:
            raise Exception
    colors[start] = 'black'


with open('output.txt', 'w') as output_file:
    try:
        dfs(1, visited, graph)
        print(0, file=output_file)
    except:
        print(1, file=output_file)

print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
