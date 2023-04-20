import time
import tracemalloc
import matplotlib.pyplot as plt

input_file = open('input.txt')
n, A = map(float, input_file.readline().split())

accuracy = 10 ** (-10)


def correct(x, y):
    return abs(x - y) <= accuracy


def less(x, y):
    return x < y and not correct(x, y)


def greater(x, y):
    return x > y and not correct(x, y)


start_time = time.perf_counter()
tracemalloc.start()
heights = [0] * int(n)
heights[0] = A
answer = float('inf')
left = 0
right = heights[0]

while less(left, right):
    heights[1] = (left + right) / 2
    isNotUp = False
    print(heights)
    for i in range(2, int(n)):
        heights[i] = 2 * heights[i - 1] - heights[i - 2] + 2
        if not greater(heights[i], 0):
            isNotUp = True
            break
    if greater(heights[-1], 0):
        answer = min(answer, heights[-1])
    if isNotUp:
        left = heights[1]
    else:
        right = heights[1]
with open('output.txt', 'w') as output_file:
    print(answer, file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
plt.plot(list(range(int(n))), heights,'g-o', linewidth = 0.1, markersize = 0.1 )
plt.savefig("graph.png")
