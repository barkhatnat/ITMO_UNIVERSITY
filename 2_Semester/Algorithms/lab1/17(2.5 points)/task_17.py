import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()

input_file = open('input.txt')
n = int(input_file.readline())
desk = [[4, 6], [6, 8], [7, 9], [4, 8],
        [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]

M = [[0 for j in range(10)] for i in range(n + 1)]

for j in range(10):
    if j == 0 or j == 8:
        continue
    M[1][j] = 1
for i in range(n + 1):
    M[i][0] = 0

for i in range(2, n + 1):
    for j in range(10):
        for choosen_number in desk[j]:
            M[i][j] += M[i - 1][choosen_number]
with open('output.txt', 'w') as output_file:
    print(sum(M[n]) % (10 ** 9), file=output_file)

print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
