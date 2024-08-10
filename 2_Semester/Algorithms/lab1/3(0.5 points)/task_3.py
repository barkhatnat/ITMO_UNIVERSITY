import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()

input_file = open('input.txt')
n = int(input_file.readline())
A = list(map(int, input_file.readline().split()))
B = list(map(int, input_file.readline().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C = [A[i] * B[i] for i in range(n)]

with open('output.txt', 'w') as output_file:
    print(sum(C), file=output_file)

print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()