import re
import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()

input_file = open('input.txt')
s = input_file.readline()
numbers = [i for i in re.split('|\+|-|\*', s) if i]
signs = [i for i in re.split('\d', s) if i]


def minimal_and_maximum(i, j, max_values, min_values, signs):
    minimal = float("+inf")
    maximum = float("-inf")
    for k in range(i, j):
        if signs[k] == "+":
            a, b, c, d = max_values[i][k] + max_values[k + 1][j], max_values[i][k] + min_values[k + 1][j], min_values[i][k] + max_values[k + 1][j], min_values[i][k] + min_values[k + 1][j]
        elif signs[k] == "*":
            a, b, c, d = max_values[i][k] * max_values[k + 1][j], max_values[i][k] * min_values[k + 1][j], min_values[i][k] * max_values[k + 1][j], min_values[i][k] * min_values[k + 1][j]
        else:
            a, b, c, d = max_values[i][k] - max_values[k + 1][j], max_values[i][k] - min_values[k + 1][j], min_values[i][k] - max_values[k + 1][j], min_values[i][k] - min_values[k + 1][j]
        minimal = min(minimal, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return maximum, minimal


N = len(numbers)
min_values, max_values = [[0 for i in range(N)] for j in range(N)], [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    max_values[i][i], min_values[i][i] = int(s[i * 2]), int(s[i * 2])
for diff in range(1, N):
    for i in range(N - diff):
        j = i + diff
        max_values[i][j], min_values[i][j] = minimal_and_maximum(i, j, max_values, min_values, signs)
with open('output.txt', 'w') as output_file:
    print(max_values[0][N - 1], file=output_file)

print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
