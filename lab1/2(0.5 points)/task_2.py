import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()

input_file = open('input.txt')
d = int(input_file.readline())
m = int(input_file.readline())
n = int(input_file.readline())
stops = list(map(int, input_file.readline().split()))
stops.append(d)
curr_stop = 0
fuel = m
answer = 0
for i in range(n + 1):
    if stops[i] - curr_stop > fuel:
        if stops[i] - stops[i - 1] > m:
            answer = -1
            break
        curr_stop = stops[i - 1]
        fuel = m
        answer += 1
    fuel = fuel - (stops[i] - curr_stop)
    curr_stop = stops[i]

with open('output.txt', 'w') as output_file:
    print(answer, file=output_file)

print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
