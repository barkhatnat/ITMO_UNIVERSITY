import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()

def isThereASubset(nums, n, len_of_subset):
    N_index = n - 1
    if len_of_subset == 0:
        return True
    if N_index < 0 or len_of_subset < 0:
        return False
    include = isThereASubset(nums, N_index - 1, len_of_subset - nums[N_index])
    if include:
        return True
    exclude = isThereASubset(nums, N_index - 1, len_of_subset)
    return exclude


def counter(S):
    first_part = []
    second_part = []
    for i in sorted(S, reverse=True):
        if sum(S) // 2 >= sum(first_part) + i:
            first_part.append(i)
        else:
            second_part.append(i)
    return first_part


input_file = open('input.txt')
n = int(input_file.readline())
nums = list(map(int, input_file.readline().split()))
with open('output.txt', 'w') as output_file:
    if sum(nums) % 2 == 0:
        if isThereASubset(nums, n, sum(nums) // 2):
            print(len(counter(nums)), file=output_file)
            print(*counter(nums), file=output_file)
    else:
        print(-1, file=output_file)

print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()