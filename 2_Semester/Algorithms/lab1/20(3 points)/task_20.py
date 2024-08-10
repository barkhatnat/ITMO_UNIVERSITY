import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()

input_file = open('input.txt')
N, K = map(int, input_file.readline().split())
S = input_file.readline()

M = [[0 if i >= j else 1 for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if i > j:
            M[i][j] = -1
        if j - 1 - i == 1:
            if S[i:j][0] == S[i:j][-1]:
                M[i][j - 1] = 0
            else:
                M[i][j - 1] = 1
for r in range(2, N):
    for i in range(N):
        for j in range(i + 1, N + 1):
            if j - 1 - i == r:
                if S[i:j][0] == S[i:j][-1]:
                    M[i][j - 1] = M[i + 1][j - 1 - 1]
                else:
                    M[i][j - 1] = M[i + 1][j - 1 - 1] + 1


c = 0
for i in range(N):
    for j in range(N):
        if 0 <= M[i][j] <= K:
            c += 1
with open('output.txt', 'w') as output_file:
    print(c, file=output_file)

print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
