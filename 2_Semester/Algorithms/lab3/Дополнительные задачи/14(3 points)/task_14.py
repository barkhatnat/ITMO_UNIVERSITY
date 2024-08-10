import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()

input_file = open('input.txt')
village_count = int(input_file.readline())
buses = [[] for _ in range(village_count + 1)]
start, finish = map(int, input_file.readline().split())
trip_count = int(input_file.readline())
for i in range(trip_count):
    start_village, t1, finish_village, t2 = map(int, input_file.readline().split())
    buses[start_village].append([t1, finish_village, t2])

inf = float('inf')
times = [inf] * (village_count + 1)
times[start] = 0
visited = [False] * (village_count + 1)
while True:
    min_time = inf
    for i in range(1, village_count + 1):
        if not visited[i] and times[i] < min_time:
            min_time = times[i]
            min_village = i
    if min_time == inf:
        break
    start_village = min_village
    visited[start_village] = True
    for t1, finish_village, t2 in buses[start_village]:
        if times[start_village] <= t1 and t2 <= times[finish_village]:
            times[finish_village] = t2

with open('output.txt', 'w') as output_file:
    if times[finish] == inf:
        print('-1', file=output_file)
    else:
        print(times[finish], file=output_file)
print(time.perf_counter() - t_start)
print(float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
