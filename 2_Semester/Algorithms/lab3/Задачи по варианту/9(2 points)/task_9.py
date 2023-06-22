import time
import tracemalloc


def bellman_ford(n, S, edges):
    dist = [float('inf')] * (n + 1)
    dist[S] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                no_inf_dist = [i for i in dist if isinstance(i, int)]
                if sum(no_inf_dist) < 0:
                    return 1
    return 0


start_time = time.perf_counter()
tracemalloc.start()
input_file = open('input.txt')
vertices, edges = map(int, input_file.readline().split())
values = [tuple(map(int, input_file.readline().split())) for _ in range(edges)]
with open('output.txt', 'w') as output_file:
    print(bellman_ford(vertices, 1, values), file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
