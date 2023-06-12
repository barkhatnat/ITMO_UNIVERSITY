import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()
input_file = open('input.txt')
p = input_file.readline()[:-1]
t = input_file.readline()
len_p = len(p)
len_t = len(t)
i = 0
count = 0
start_points = []
while i < len_t - len_p + 1:
    if t[i:i + len_p] == p:
        start_points.append(i + 1)
        count += 1
    i += 1
with open('output.txt', 'w') as output_file:
    print(count, file=output_file)
    print(*start_points, file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
