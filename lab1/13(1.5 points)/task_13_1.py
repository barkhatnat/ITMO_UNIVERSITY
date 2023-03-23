import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()

input_file = open('input.txt')
n = int(input_file.readline())
nums = list(map(int, input_file.readline().split()))

def isThereASubsets(S, n, a, b, c):
    if a == 0 and b == 0 and c == 0:
        return True
    if n < 0:
        return False
    part_a = False
    if a - S[n] >= 0:
        part_a = isThereASubsets(S, n - 1, a - S[n], b, c)
    part_b = False
    if not part_a and (b - S[n] >= 0):
        part_b = isThereASubsets(S, n - 1, a, b - S[n], c)
    part_c = False
    if (not part_a and not part_b) and (c - S[n] >= 0):
        part_c = isThereASubsets(S, n - 1, a, b, c - S[n])
    return part_a or part_b or part_c


with open('output.txt', 'w') as output_file:
    if sum(nums) % 3 == 0 and isThereASubsets(nums, n - 1, sum(nums) // 3, sum(nums) // 3, sum(nums) // 3):
        print(1, file=output_file)
    else:
        print(0, file=output_file)

print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
